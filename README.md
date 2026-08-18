# Jacqueline Suling Balan — QA Engineer

> I help teams release software with confidence by finding risks early, communicating defects clearly, and building focused coverage around real customer journeys.

[![Portfolio](https://img.shields.io/badge/portfolio-QA%20testing-6d28d9)](https://github.com/Jacqueline05/qa-portfolio)
[![Focus](https://img.shields.io/badge/focus-quality%20engineering-0f766e)](https://github.com/Jacqueline05/qa-portfolio)

## Quick navigation

- [Professional profile](#professional-profile)
- [What I bring](#what-i-bring)
- [Featured case study](#featured-case-study-checkout-reliability)
- [Skills and tools](#skills-and-tools)
- [Work samples](#work-samples)
- [Automation and API assets](#automation-and-api-assets)
- [QA process](#qa-process)
- [Repository structure](#repository-structure)
- [Contact](#contact)

## Professional profile

I am a Quality Assurance Engineer with 3+ years of experience across enterprise manual testing, test automation, database validation, Linux systems, and CI/CD workflows. My approach combines structured test design with exploratory investigation and root-cause analysis.

This portfolio demonstrates how I work as part of an Agile delivery team:

- Clarify acceptance criteria and identify risks before implementation is complete.
- Design coverage around critical user journeys and failure modes.
- Combine exploratory testing with repeatable regression checks.
- Report defects with clear impact, evidence, reproduction steps, and priority.
- Collaborate with developers and product owners on risk-based release decisions.
- Improve the test process after incidents instead of treating defects as isolated events.

## Professional experience

### Quality Assurance Engineer — Enterprise Technology Environment

**September 2024 – Present**

- Execute end-to-end manual, exploratory, functional, smoke, regression, and risk-based testing.
- Design test plans and detailed test cases aligned with quality and compliance expectations.
- Build and maintain Python-based Automated Test Frameworks using pytest, Playwright, and Cucumber/BDD.
- Perform database-level validation with SQL and MySQL tools to verify data integrity, schema compliance, and state persistence.
- Manage test cases, sprint work, and defect lifecycles using Azure DevOps and Jira.
- Investigate logs, database records, and test behavior to identify root causes and reduce flaky tests.

### Systems Engineer

**January 2023 – August 2024**

- Administer Linux environments and investigate system, service, and network issues.
- Create Bash and Perl scripts for log parsing and repeatable operational tasks.
- Support directory services, access control, service dependencies, and operational troubleshooting.

This experience gives me a broader debugging perspective: I can investigate not only what the UI displays, but also the API, database, logs, and infrastructure behind it.

### Programmer — Geospatial and Web Solutions

**September 2022 – November 2022**

- Deployed geospatial data infrastructure using Docker, PostGIS, GeoNode, and Ubuntu.
- Developed survey tools and web modules using Flutter, Dart, Android Studio, and web technologies.
- Worked across application code, databases, containers, and Linux environments to deliver working technical solutions.

This early software engineering experience supports my QA work by helping me understand application architecture, data flow, deployment environments, and the practical impact of defects.

## Testing approach

```text
Understand requirements → Identify risk → Design coverage
        ↓                         ↓
  Exploratory testing       API and UI validation
        ↓                         ↓
  Report and triage → Regression → Release recommendation
                                      ↓
                              Learn and improve
```

## What I bring

- **Risk-based testing:** prioritize the failures that can cost customers money, trust, or access.
- **Full workflow coverage:** connect UI behavior, API responses, data, and release risk.
- **Actionable communication:** write bug reports that developers can reproduce and fix quickly.
- **Quality mindset:** test unhappy paths, recovery behavior, accessibility, and cross-device experiences—not only the happy path.

## Featured case study: checkout reliability

The ShopEasy checkout examples tell one complete QA story:

1. The [test plan](test-cases/01-test-plan.md) defines scope, risks, and release criteria.
2. The [test cases](test-cases/03-test-cases.md) cover success, validation, and declined payment.
3. The [bug reports](bug-reports/04-bug-reports.md) demonstrate evidence-based defect reporting.
4. The [API cases](api-testing/08-api-test-cases.md) verify idempotency and authorization.
5. The [test summary](reports/13-test-summary-report.md) makes a clear go/no-go recommendation.
6. The [incident review](bug-reports/15-incident-review.md) turns a production failure into preventive action.

This is the kind of connected thinking I bring to a QA engineering team.

## Skills demonstrated

| Area | Evidence in this portfolio |
|---|---|
| Manual testing | Test plans, scenarios, cases, exploratory charter |
| Defect management | Reproducible bug reports with severity, impact, and evidence |
| API testing | REST coverage, status codes, schemas, negative cases, idempotency |
| Regression and release | Prioritized checklist, traceability matrix, test summary |
| Accessibility | Keyboard, focus, error messaging, zoom, contrast checks |
| Mobile testing | Device/browser matrix and responsive checks |
| Test strategy | Risk scoring, data strategy, entry/exit criteria |
| Quality improvement | Post-release incident review and corrective actions |

## Skills and tools

| Capability | Portfolio evidence | Typical tools |
|---|---|---|
| Test design | Plans, scenarios, cases, checklists | Markdown, Jira-style workflows |
| UI automation | Critical checkout smoke test | Python, pytest, Playwright, Selenium |
| API testing | REST plan, negative cases, idempotency | Postman, REST clients, Python |
| Defect reporting | Reproducible reports and triage details | Jira-style bug lifecycle |
| Accessibility | Keyboard, focus, error, zoom, contrast review | Browser DevTools, screen readers |
| Compatibility | Mobile device and browser matrix | Chrome, Edge, Safari, responsive viewports |
| Release quality | Traceability, risk scoring, summary report | Azure DevOps, Jira, CI/CD |
| Test data | Synthetic users, products, coupons, payments | Fixtures, API setup, reset strategy |
| Database testing | Integrity, schema, and state persistence checks | SQL, MySQL, SQLyog |
| Systems diagnostics | Logs, services, access, and environment investigation | RHEL, Oracle Linux, Bash, Perl, Docker |

## Work samples

| # | Sample | Skills demonstrated |
|---|---|---|
| 01 | [Test Plan](test-cases/01-test-plan.md) | Scope, risks, strategy, entry/exit criteria |
| 02 | [Test Scenarios](test-cases/02-test-scenarios.md) | Requirement decomposition and coverage |
| 03 | [Test Cases](test-cases/03-test-cases.md) | Preconditions, steps, expected results |
| 04 | [Bug Reports](bug-reports/04-bug-reports.md) | Reproduction, severity, evidence, triage |
| 05 | [Regression Checklist](test-cases/05-regression-checklist.md) | Release confidence and prioritization |
| 06 | [Exploratory Test Charter](test-cases/06-exploratory-testing.md) | Session-based exploratory testing |
| 07 | [API Test Plan](api-testing/07-api-test-plan.md) | REST coverage and contract validation |
| 08 | [API Test Cases](api-testing/08-api-test-cases.md) | Status codes, schemas, negative testing |
| 09 | [UI Accessibility Review](accessibility/09-accessibility-review.md) | WCAG-focused manual checks |
| 10 | [Mobile Test Matrix](test-cases/10-mobile-test-matrix.md) | Device, browser, and responsive coverage |
| 11 | [Requirements Traceability Matrix](test-cases/11-traceability-matrix.md) | Requirement-to-test mapping |
| 12 | [Test Data Plan](test-cases/12-test-data-plan.md) | Safe, repeatable test data |
| 13 | [Test Summary Report](reports/13-test-summary-report.md) | Results, metrics, release recommendation |
| 14 | [Risk-Based Testing](test-cases/14-risk-based-testing.md) | Risk scoring and test prioritization |
| 15 | [Post-release Incident Review](bug-reports/15-incident-review.md) | Root cause, containment, prevention |

## Automation and API assets

See [`automation-scripts/checkout_test.py`](automation-scripts/checkout_test.py) for a Python/pytest Playwright example, and [`automation-scripts/checkout.spec.ts`](automation-scripts/checkout.spec.ts) for a TypeScript variant.

The [`postman/`](postman/) folder contains a safe, fictional REST collection for catalog, cart, and order validation. The collection uses environment variables rather than real credentials or payment data.

The [portfolio validation workflow](.github/workflows/portfolio-validation.yml) checks that the repository's JSON assets remain valid whenever changes are pushed or opened as a pull request.

## QA process

### Before testing

- Review requirements, acceptance criteria, designs, and dependencies.
- Identify high-impact risks such as payment, authorization, data loss, and accessibility.
- Define test data, environments, entry criteria, and exit criteria.

### During testing

- Start with smoke coverage before deeper functional testing.
- Combine positive, negative, boundary, exploratory, and recovery scenarios.
- Validate both user-visible behavior and API responses.
- Record actual results, evidence, environment, and defect impact.

### Before release

- Review critical-path regression results and unresolved defects.
- Confirm traceability for high-risk requirements.
- Communicate residual risk and make a clear release recommendation.
- Preserve repeatable tests and test data for the next iteration.

## Portfolio assumptions and limitations

ShopEasy is a fictional e-commerce application created for demonstration. The API endpoints, payment numbers, order IDs, and defects are examples only. The Playwright and Postman assets show test design and structure; they are not connected to a public production system.

## Repository structure

```text
qa-portfolio/
├── test-cases/          # Plans, scenarios, regression, exploratory, and test data
├── bug-reports/         # Reproducible defects and incident reviews
├── api-testing/         # REST API plans and test cases
├── accessibility/       # WCAG-focused review
├── reports/             # Release and test summary reporting
├── automation-scripts/  # Playwright examples
├── postman/             # API collection with safe placeholders
└── .github/workflows/   # Portfolio validation in CI
```

## Application under test

**ShopEasy** is a fictional online store with product search, accounts, cart, checkout, payments, order history, and an administrator product catalog.

All data and defects are fictional examples created for demonstration purposes. No confidential company information is included.

## How to review

Start with the checkout case study above. Then review the [risk-based testing approach](test-cases/14-risk-based-testing.md) and [test data plan](test-cases/12-test-data-plan.md) to see how I think about coverage, repeatability, and release confidence.

## Contact

Available for QA Engineer, Software Test Engineer, and Quality Engineer opportunities.

- GitHub: [github.com/Jacqueline05](https://github.com/Jacqueline05)
- LinkedIn: Jacqueline Suling
- Email: [jacqsuling@gmail.com](mailto:jacqsuling@gmail.com)
