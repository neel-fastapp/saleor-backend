from datetime import datetime

import graphene

from .....order import OrderStatus
from .....order.models import Order, OrderEvent, OrderLine
from ....tests.utils import get_graphql_content

ORDER_BULK_CREATE = """
    mutation OrderBulkCreate(
        $orders: [OrderBulkCreateInput!]!,
    ) {
        orderBulkCreate(orders: $orders) {
            count
            results {
                order {
                    id
                    discount {
                        amount
                    }
                    discountName
                    redirectUrl
                    lines {
                        productName
                        productSku
                        quantity
                        id
                    }
                    billingAddress{
                        city
                        streetAddress1
                        postalCode
                    }
                    events {
                        message
                    }
                    weight {
                        value
                    }
                    displayGrossPrices
                    fulfillments {
                        lines {
                            quantity
                            orderLine {
                                id
                            }
                        }
                    }
                }
                errors {
                    field
                    message
                    code
                }
            }
        }
    }
"""


def test_order_bulk_create(
    staff_api_client,
    permission_manage_orders,
    channel_PLN,
    graphql_address_data,
    customer_user,
    warehouses,
    variant,
    default_tax_class,
    shipping_method_channel_PLN,
    app,
    stock,
):
    # given
    orders_count = Order.objects.count()
    order_lines_count = OrderLine.objects.count()
    order_events = OrderEvent.objects.count()

    shipping_method = shipping_method_channel_PLN
    user = {
        "id": graphene.Node.to_global_id("User", customer_user.id),
        "email": None,
    }
    delivery_method = {
        # "warehouseId": graphene.Node.to_global_id("Warehouse", warehouses[0].id),
        "shippingMethodId": graphene.Node.to_global_id(
            "ShippingMethod", shipping_method.id
        ),
        "shippingTaxClassId": graphene.Node.to_global_id(
            "TaxClass", default_tax_class.id
        ),
    }
    line_1 = {
        "variantId": graphene.Node.to_global_id("ProductVariant", variant.id),
        "createdAt": datetime.now(),
        "isShippingRequired": True,
        "isGiftCard": False,
        "quantity": 5,
        "quantityFulfilled": 0,
        "totalPrice": {
            "gross": 100,
            "net": 80,
            "currency": "PLN",
        },
        "undiscountedTotalPrice": {
            "gross": 100,
            "net": 80,
            "currency": "PLN",
        },
        "taxRate": 20,
        "taxClassId": graphene.Node.to_global_id("TaxClass", default_tax_class.id),
    }
    note_1 = {
        "message": "Test message",
        "date": datetime.now(),
        "userId": graphene.Node.to_global_id("User", customer_user.id),
        # "appId": graphene.Node.to_global_id("App", app.id),
    }
    order_1 = {
        "channel": channel_PLN.slug,
        "createdAt": datetime.now(),
        "status": OrderStatus.DRAFT,
        "user": user,
        "billingAddress": graphql_address_data,
        "shippingAddress": graphql_address_data,
        "languageCode": "PL",
        "deliveryMethod": delivery_method,
        "lines": [line_1],
        "notes": [note_1],
        "weight": "10.15",
    }
    staff_api_client.user.user_permissions.add(permission_manage_orders)
    variables = {"orders": [order_1]}

    # when
    response = staff_api_client.post_graphql(ORDER_BULK_CREATE, variables)
    content = get_graphql_content(response)

    # then
    assert content["data"]["orderBulkCreate"]["count"] == 1
    data = content["data"]["orderBulkCreate"]["results"]
    assert not data[0]["errors"]
    order = data[0]["order"]
    assert order["lines"]
    assert order["events"][0]["message"] == "Test message"
    assert order["weight"]["value"] == 10.15
    assert order["displayGrossPrices"]

    assert Order.objects.count() == orders_count + 1
    assert OrderLine.objects.count() == order_lines_count + 1
    assert OrderEvent.objects.count() == order_events + 1
