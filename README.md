![Saleor Commerce - A GraphQL-first platform for perfectionists](https://user-images.githubusercontent.com/249912/71523206-4e45f800-28c8-11ea-84ba-345a9bfc998a.png)

<div align="center">
  <h1>Saleor Commerce</h1>
</div>

<div align="center">
  <strong>Customer-centric e-commerce on a modern stack</strong>
</div>

<div align="center">
  A headless, GraphQL commerce platform delivering ultra-fast, dynamic, personalized shopping experiences. Beautiful online stores, anywhere, on any device.
</div>

<br>

<div align="center">
  Join our active, engaged community: <br>
  <a href="https://saleor.io/">Website</a>
  <span> | </span>
  <a href="https://twitter.com/getsaleor">Twitter</a>
  <span> | </span>
  <a href="https://github.com/saleor/saleor/discussions">GitHub Discussions</a>
</div>

<div align="center">
   <a href="https://saleor.io/blog/">Blog</a>
  <span> | </span>
  <a href="https://saleor.typeform.com/to/JTJK0Nou">Subscribe to newsletter</a>
</div>

<br>

<div align="center">
  <a href="http://codecov.io/github/saleor/saleor?branch=master">
    <img src="http://codecov.io/github/saleor/saleor/coverage.svg?branch=master" alt="Codecov" />
  </a>
  <a href="https://docs.saleor.io/">
    <img src="https://img.shields.io/badge/docs-docs.saleor.io-brightgreen.svg" alt="Documentation" />
  </a>
  <a href="https://github.com/python/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
  </a>
</div>

## Table of Contents

- [What makes Saleor special?](#what-makes-saleor-special)
- [Features](#features)
- [Installation](#installation)
- [Documentation](#documentation)
- [Demo](#demo)
- [Contributing](#contributing)
- [Your feedback](#your-feedback)
- [License](#license)

## What makes Saleor special?

Saleor is a rapidly-growing open-source e-commerce platform that serves high-volume companies. Designed from the ground up to be extensible, headless, and composable.

Learn more about [architecture](https://docs.saleor.io/docs/3.x/overview/architecture).

## Features

- **Headless / API first**: Build mobile apps, custom storefronts, POS, automation, etc
- **Extensible**: Build anything with webhooks, apps, metadata, and attributes
- **GraphQL API**: Get many resources in a single request and [more](https://graphql.org/)
- **Multichannel**: Per channel control of pricing, currencies, stock, product, and more
- **Enterprise ready**: Secure, scalable, and stable. Battle-tested by big brands
- **CMS**: Content is king, that's why we have a kingdom built-in
- **Dashboard**: User friendly, fast, and productive. (Decoupled project [repo](https://github.com/saleor/saleor-dashboard) )
- **Global by design** Multi-currency, multi-language, multi-warehouse, tutti multi!
- **Orders**: A comprehensive system for orders, dispatch, and refunds
- **Cart**: Advanced payment and tax options, with full control over discounts and promotions
- **Payments**: Flexible API architecture allows integration of any payment method
- **SEO**: Packed with features that get stores to a wider audience
- **Cloud**: Optimized for deployments using Docker

Saleor is free and always will be.
Help us out… If you love free stuff and great software, give us a star! 🌟

![Saleor Storefront - React-based PWA e-commerce storefront](https://user-images.githubusercontent.com/249912/71527146-5b6be280-28da-11ea-901d-eb76161a6bfb.png)
![Saleor Dashboard - Modern UI for managing your e-commerce](https://user-images.githubusercontent.com/249912/71523261-8a795880-28c8-11ea-98c0-6281ea37f412.png)

## Installation

[See the Saleor docs](https://docs.saleor.io/docs/3.x/developer/installation) for step-by-step installation and deployment instructions.

Note:
The `main` branch is the development version of Saleor and it may be unstable. To use the latest stable version, download it from the [Releases](https://github.com/saleor/saleor/releases/) page or switch to a release tag.

The current production-ready version is 3.x and you should use this version for all three components:

- Saleor: https://github.com/saleor/saleor/releases/
- Dashboard: https://github.com/saleor/saleor-dashboard/releases/
- Storefront: https://github.com/saleor/react-storefront/releases/

Steps to run:

```
# Migrate db
docker-compose run --rm api python3 manage.py migrate

# (Optional) Populate db
docker-compose run --rm api python3 manage.py populatedb

# Create super user
docker-compose run --rm api python3 manage.py createsuperuser

# Start the processes
docker-compose up

```

## Documentation

Saleor documentation is available here: [docs.saleor.io](https://docs.saleor.io)

To contribute, please see the [`saleor/saleor-docs` repository](https://github.com/saleor/saleor-docs/).

## Saleor Platform

The easiest way to run all components of Saleor (API, storefront, and dashboard) together on your local machine is to use the [saleor-platform](https://github.com/saleor/saleor-platform) project. Go to that repository for instructions on how to use it.

[View saleor-platform](https://github.com/saleor/saleor-platform)

## Storefront

An open-source storefront in React.js with Next.js. Built for Headless Commerce, using a modern stack with TypeScript, GraphQL, Apollo, and Tailwind CSS.

[React Storefront Repository](https://github.com/saleor/react-storefront)

[View Storefront Demo](https://reactstorefront.vercel.app/)

## Dashboard

For the dashboard go to the [saleor-dashboard](https://github.com/saleor/saleor-dashboard) repository.

[View dashboard demo](https://demo.saleor.io/dashboard/)

## Demo

Want to see Saleor in action?

- [View React Storefront](https://demo.saleor.io/)
- [View Dashboard (admin area)](https://demo.saleor.io/dashboard/)

## License

Disclaimer: Everything you see here is open and free to use as long as you comply with the [license](https://github.com/saleor/saleor/blob/master/LICENSE). There are no hidden charges. We promise to do our best to fix bugs and improve the code.
