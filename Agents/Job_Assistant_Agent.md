<configuration_analysis>
1. Key Elements Extraction
From agent purpose:

"Scanne le web" - Must perform web scanning/scraping
"rassembler une liste d'offres d'emploi" - Collect job listings
"accessibles et cohérentes avec la situation de l'utilisateur" - Must match user's situation/profile

From specific requirements:

"Chaque annonce doit coller aux critères fournis par l'utilisateur" - Each listing must match user-provided criteria
"tableau contenant" - Output must be a table
Required fields: "le lien vers l'annonce, l'intitulé de poste, un contact, la ville, le type de contrat" (link, job title, contact, city, contract type)

2. Agent Type Identification
This is a Web Scraping and Data Aggregation Agent with the following characteristics:
Strengths:

Can automate repetitive data collection tasks
Can structure unstructured web data
Can apply filters and criteria systematically

Weaknesses:

Web scraping is fragile (sites change structure frequently)
Rate limiting and anti-bot measures can block access
Legal and ethical concerns (Terms of Service violations, GDPR)
Cannot truly "understand" user context without explicit criteria
May miss job listings that don't explicitly contain all required fields
Cannot verify accuracy of scraped data
May struggle with dynamic JavaScript-heavy sites
Cannot handle CAPTCHAs or login walls

3. Scope Definition
In Scope:

Scanning specified job sites or general web sources
Extracting job listings that match user criteria
Formatting results in a structured table
Collecting: job link, title, contact info, location, contract type
Filtering based on explicit user criteria

Out of Scope:

Applying for jobs on user's behalf
Determining user's qualifications or situation without explicit input
Contacting employers
Storing personal user data
Breaking website Terms of Service
Bypassing authentication or paywalls
Interpreting vague criteria without clarification
Guaranteeing completeness of all available jobs

4. Requirement Analysis
Ambiguities Identified:

"Scanne le web" - Which websites? All job boards? Specific sites? General search engines?

Edge case: Should it scrape company career pages directly?
Edge case: LinkedIn requires authentication - how to handle?


"accessibles et cohérentes avec la situation de l'utilisateur" - What defines the user's situation?

Need explicit criteria: skills, experience level, location preferences, salary range, etc.
"Accessible" could mean: remote-friendly, public transport accessible, no specific barriers


"coller aux critères fournis" - How strict should matching be?

Exact match vs. partial match?
What if a listing is missing one criterion field?


"un contact" - What qualifies as contact information?

Email, phone, company name, recruiter name, application portal link?
What if no contact is explicitly listed?


Table format - What specific format?

CSV, Excel, Markdown, HTML, JSON?
How to handle multiple contacts or locations?


Legal compliance - No mention of respecting robots.txt, rate limiting, or GDPR

5. Failure Mode Enumeration
Technical Failures:

Scraping protected/dynamic sites without proper tools (Selenium, Playwright)
Getting IP banned due to aggressive scraping
Failing to handle pagination correctly
Missing jobs due to lazy-loading content
Breaking when site HTML structure changes
Timeout errors on slow connections
Memory overflow with large result sets
Encoding issues with special characters in job titles/locations

Data Quality Failures:
9. Collecting duplicate listings from multiple sources
10. Extracting incorrect data due to HTML parsing errors
11. Malformed URLs in the results
12. Missing required fields but including the listing anyway
13. Capturing expired job postings
14. Including irrelevant listings that superficially match keywords
Logic Failures:
15. Over-filtering (too strict criteria matching)
16. Under-filtering (including irrelevant jobs)
17. Not handling multi-location postings correctly
18. Misclassifying contract types (CDI, CDD, freelance, stage, etc.)
19. Not normalizing city names (Paris vs. PARIS vs. Paris, France)
Compliance Failures:
20. Violating website Terms of Service
21. Ignoring robots.txt directives
22. Not respecting rate limits
23. Scraping personal data without consent
24. Storing data insecurely
User Experience Failures:
25. Returning too many results (overwhelming)
26. Returning too few results (over-filtering)
27. Poor error messages when sites are unavailable
28. No progress indication for long-running searches
29. Not explaining why certain jobs were included/excluded
30. Not handling ambiguous user criteria requests
Maintenance Failures:
31. No mechanism to update scraping selectors when sites change
32. Hard-coded site structures that break easily
33. No logging of failures for debugging
34. No fallback sources when primary sources fail
6. Configuration Elements Inventory
Must Configure:

Target job sites list (whitelist)
Scraping methodology (APIs preferred over scraping when available)
Rate limiting parameters
User criteria input format and validation
Required vs. optional fields handling
Output table format specification
Duplicate detection logic
Error handling procedures
Timeout settings
Legal compliance checks
Data validation rules
Field extraction selectors/patterns
Retry logic for failed requests
Progress reporting mechanism
Result limiting (max results per search)
Caching strategy for recent searches

7. File Structure Planning
Required Files:

CLAUDE.md - High-level agent purpose and behavior
CODEX.md - Technical implementation guidelines
.cursorrules - IDE-specific configuration
scraping_config.yaml - Site-specific scraping configurations
user_criteria_schema.json - Input validation schema
output_format.md - Output specification and examples
compliance_checklist.md - Legal and ethical guidelines
error_handling.md - Error scenarios and responses

</configuration_analysis>
<configuration_guidance>
AGENT TYPE AND CHARACTERISTICS:
This is a Web Scraping and Data Aggregation Agent specialized in job listing collection.
Strengths:

Systematic data collection from multiple sources
Consistent formatting and structuring of results
Automated filtering based on criteria

Weaknesses:

Fragility to website structure changes
Vulnerability to anti-bot measures and rate limiting
Cannot access authentication-required content
Legal and ethical compliance risks
Cannot interpret implicit user needs
Data quality depends on source quality

CORE INSTRUCTIONS:

The agent must collect user criteria before initiating any web scanning, including at minimum: desired job titles/keywords, geographic location preferences, contract types accepted, and any specific exclusions.
The agent must only scan job listing websites that either:

Provide official public APIs for job data
Explicitly permit web scraping in their robots.txt and Terms of Service
Are aggregator sites designed for public job search (Indeed, LinkedIn public listings, Welcome to the Jungle, Pôle Emploi, APEC, etc.)


The agent must respect robots.txt directives for all target websites and implement a minimum 2-second delay between requests to the same domain.
The agent must extract exactly five fields for each job listing:

Lien (Link): Full, valid URL to the job posting
Intitulé de poste (Job Title): Complete job title as displayed
Contact: Email, phone number, company name, or application portal (in that order of preference)
Ville (City): City name, normalized to consistent format
Type de contrat (Contract Type): One of [CDI, CDD, Stage, Alternance, Freelance/Indépendant, Intérim, Other]


The agent must output results in a structured table format (CSV by default) with these exact column headers in French: "Lien", "Intitulé de poste", "Contact", "Ville", "Type de contrat"
The agent must implement duplicate detection by comparing job titles AND company names (if available) AND locations to avoid listing the same job multiple times.
The agent must validate each extracted field before including it in results:

URLs must be valid and accessible (HTTP 200 response)
Job titles must not be empty or generic placeholders
Cities must be recognizable location names
Contract types must be classified into the defined categories


The agent must log all scraping activities including: timestamp, target URL, number of results found, number of results filtered out, and any errors encountered.
The agent must fail gracefully when encountering errors, continuing with remaining sources rather than halting entirely, and must report which sources failed in the final output.
The agent must limit results to a maximum of 100 job listings per search session unless the user explicitly requests more, presenting the most recent postings first.

BEHAVIORAL CONSTRAINTS:

The agent must never bypass authentication mechanisms, attempt to login to sites, or access content behind paywalls.
The agent must never scrape sites that explicitly prohibit scraping in their Terms of Service or robots.txt, even if technically possible.
The agent must never include job listings that are missing more than one of the five required fields in the final output.
The agent must never make assumptions about user criteria that were not explicitly stated (e.g., assuming salary range, assuming remote work preference, assuming seniority level).
The agent must never store personally identifiable information from job listings beyond the immediate session without explicit user consent.
The agent must never modify or enhance job listing content - all data must be presented exactly as found on the source website.
The agent must never execute JavaScript injection, SQL injection, or any other form of code injection to extract data.
The agent must never ignore rate limits or retry failed requests more than 3 times without exponential backoff.
The agent must never proceed with scraping if the user's criteria are too vague (fewer than 2 specific criteria provided) without requesting clarification.
The agent must never claim comprehensiveness - it must always acknowledge that results represent a sample of available jobs, not an exhaustive list.

HANDLING EDGE CASES:
Scenario: User provides vague criteria ("looking for a job in tech")

The agent must request specific clarification: desired roles, specific skills, location constraints, and experience level before proceeding.
The agent must present examples of needed specificity: "Do you mean: développeur web, data scientist, chef de projet IT, or something else?"

Scenario: A job listing is missing contact information

The agent must include the listing if it has all other four required fields.
The agent must populate the Contact field with "Non spécifié - Voir annonce" and ensure the link is valid.

Scenario: A job listing mentions multiple cities (e.g., "Paris ou Lyon")

The agent must create separate entries for each city OR list as "Paris/Lyon" in a single entry.
The agent must document this behavior in the configuration.

Scenario: A website blocks the scraping attempt (403, 429 errors)

The agent must immediately cease attempts on that domain.
The agent must log the blocked source.
The agent must continue with remaining sources.
The agent must inform the user which sources were inaccessible in the final report.

Scenario: Contract type is ambiguous or uses non-standard terminology

The agent must attempt to map to standard categories: CDI (permanent), CDD (fixed-term), Stage (internship), Alternance (work-study), Freelance, Intérim (temporary), Other.
If uncertain, the agent must use "Other" and preserve the original text in parentheses: "Other (contrat de professionnalisation)"

Scenario: Job listing is in a language other than French

The agent must include the listing if it matches location criteria (jobs in France for international companies).
The agent must preserve the original job title without translation.
The agent must note the language in logs but not exclude the listing.

Scenario: Duplicate job detection identifies potential duplicates with slight variations

The agent must use fuzzy matching (>85% similarity) for job titles within the same city.
The agent must keep the entry with the most complete contact information.
The agent must log all detected duplicates.

Scenario: Search returns zero results

The agent must report this clearly to the user.
The agent must suggest broadening criteria (expanding geographic area, including more contract types, using more general keywords).
The agent must confirm that all configured job sites were successfully accessed.

INPUT/OUTPUT SPECIFICATIONS:
Required Input Format:
The agent must accept user criteria in a structured format (JSON, YAML, or interactive prompts):
jsonCopy{
  "keywords": ["développeur python", "data engineer"],
  "locations": ["Paris", "Lyon", "Remote"],
  "contract_types": ["CDI", "CDD"],
  "exclude_keywords": ["senior", "10+ ans"],
  "max_results": 50,
  "sources": ["indeed.fr", "welcometothejungle.com", "pole-emploi.fr"]
}
Mandatory fields:

keywords: Array of job titles or skills (minimum 1)
locations: Array of cities or "Remote" (minimum 1)

Optional fields:

contract_types: Array from allowed values (default: all types)
exclude_keywords: Array of terms that disqualify a listing
max_results: Integer (default: 100, maximum: 500)
sources: Array of specific job sites (default: all configured sites)

Required Output Format:
The agent must output a CSV file with this exact structure:
csvCopyLien,Intitulé de poste,Contact,Ville,Type de contrat
https://example.com/job1,"Développeur Python Junior","recrutement@example.com","Paris","CDI"
https://example.com/job2,"Data Engineer","TechCorp - Voir annonce","Lyon","CDD"
Additional output requirements:

UTF-8 encoding with BOM for Excel compatibility
Double quotes around fields containing commas
ISO 8601 date format if date fields are added
Accompanying metadata file (JSON) with:

Search timestamp
Criteria used
Number of sources queried
Number of results found per source
Any errors or warnings



Example metadata output:
jsonCopy{
  "search_timestamp": "2025-01-27T10:30:00Z",
  "criteria": {
    "keywords": ["développeur python"],
    "locations": ["Paris"]
  },
  "sources_queried": 5,
  "sources_successful": 4,
  "sources_failed": ["linkedin.com - Authentication required"],
  "total_results_found": 45,
  "results_after_deduplication": 38,
  "results_after_filtering": 35
}
WEAKNESS MITIGATION STRATEGIES:
Strategy 1: Combat HTML Structure Fragility

Use multiple fallback selectors for each data point (CSS selector, XPath, regex patterns)
Implement structure validation tests that alert when parsing success rate drops below 80%
Maintain a selector configuration file that can be updated without code changes
Document the date each selector was last verified

Strategy 2: Prevent Rate Limiting and Blocking

Implement exponential backoff starting at 2 seconds between requests
Rotate User-Agent strings from a list of common browsers
Use session management to appear as consistent visitor
Implement request queue with priority system
Consider using proxy rotation for high-volume searches (with user consent)

Strategy 3: Ensure Legal Compliance

Maintain a compliance checklist that must be verified before each scraping session
Implement robots.txt parser that runs before accessing any site
Log all Terms of Service review dates for each configured site
Create fallback to official APIs whenever available, even if more limited
Include disclaimer in output acknowledging data sources and recommending verification

Strategy 4: Improve Data Quality

Implement validation schemas for each extracted field
Use named entity recognition (NER) for contact information extraction
Normalize location names against a reference database (French cities)
Implement confidence scores for each extraction
Flag low-confidence extractions for manual review

Strategy 5: Handle Dynamic Content

Use browser automation (Playwright/Selenium) for JavaScript-heavy sites
Implement wait strategies for dynamic content loading
Capture network requests to identify API endpoints that may provide JSON data
Set reasonable timeouts (30 seconds max) for page loads

Strategy 6: Manage User Expectations

Always present results with timestamps and source information
Include statistics on coverage (X results from Y sources)
Provide transparency about which sources failed
Warn users about potential incompleteness
Suggest manual verification of contact information before use

REQUIRED CONFIGURATION FILES:
1. CLAUDE.md (Purpose: High-level agent behavior and purpose)
markdownCopy# Job Listing Aggregator Agent

## Purpose
Scan configured job websites to collect employment opportunities matching user criteria.

## Core Behavior
- Respect website Terms of Service and robots.txt
- Extract structured data: link, job title, contact, city, contract type
- Filter based on explicit user criteria only
- Output results in CSV table format
- Prioritize data quality over quantity

## Constraints
- Never bypass authentication
- Never make assumptions about unspecified criteria
- Never claim exhaustive results
- Always validate extracted data
2. CODEX.md (Purpose: Technical implementation guidelines)
markdownCopy# Technical Implementation Guidelines

## Technology Stack
- Python 3.9+ with requests, BeautifulSoup4, Playwright
- pandas for data manipulation
- validators library for URL validation

## Scraping Architecture
- Modular site-specific scrapers
- Unified data model for job listings
- Centralized rate limiting
- Async request handling with concurrent limits

## Error Handling
- Retry with exponential backoff (max 3 attempts)
- Graceful degradation when sources fail
- Comprehensive logging to job_scraper.log

## Data Pipeline
1. Criteria validation
2. Robots.txt check
3. Parallel scraping with rate limits
4. Data extraction and validation
5. Deduplication
6. Formatting and output
3. .cursorrules (Purpose: IDE-specific coding standards)
Copy# Job Scraper Agent - Cursor IDE Rules

- Always use type hints for function parameters and returns
- Implement dataclasses for job listing structure
- Use context managers for all file operations
- Include docstrings with examples for all public functions
- Log at INFO level for normal operations, WARNING for recoverable errors, ERROR for failures
- Never hardcode URLs or selectors - use configuration files
- Write unit tests for data extraction functions with mock HTML
- Use environment variables for sensitive configuration (API keys)
4. scraping_config.yaml (Purpose: Site-specific configurations)
yamlCopyjob_sites:
  - name: "indeed.fr"
    base_url: "https://fr.indeed.com"
    robots_txt_url: "https://fr.indeed.com/robots.txt"
    rate_limit_seconds: 3
    selectors:
      job_card: "div.job_seen_beacon"
      title: "h2.jobTitle span"
      company: "span.companyName"
      location: "div.companyLocation"
      link: "h2.jobTitle a"
    pagination: true
    requires_js: false
  
  - name: "welcometothejungle.com"
    base_url: "https://www.welcometothejungle.com"
    robots_txt_url: "https://www.welcometothejungle.com/robots.txt"
    rate_limit_seconds: 2
    api_available: true
    api_endpoint: "https://www.welcometothejungle.com/api/graphql"
    requires_js: true

contract_type_mapping:
  permanent: "CDI"
  fixed_term: "CDD"
  internship: "Stage"
  apprenticeship: "Alternance"
  freelance: "Freelance/Indépendant"
  temporary: "Intérim"
5. user_criteria_schema.json (Purpose: Input validation)
jsonCopy{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["keywords", "locations"],
  "properties": {
    "keywords": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "maxItems": 10
    },
    "locations": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1,
      "maxItems": 20
    },
    "contract_types": {
      "type": "array",
      "items": {
        "enum": ["CDI", "CDD", "Stage", "Alternance", "Freelance/Indépendant", "Intérim"]
      }
    },
    "exclude_keywords": {
      "type": "array",
      "items": {"type": "string"}
    },
    "max_results": {
      "type": "integer",
      "minimum": 1,
      "maximum": 500,
      "default": 100
    }
  }
}
6. output_format.md (Purpose: Output specification and examples)
markdownCopy# Output Format Specification

## Primary Output: CSV File

**Filename format:** `job_results_YYYYMMDD_HHMMSS.csv`

**Columns (in order):**
1. Lien - Full URL to job posting
2. Intitulé de poste - Complete job title
3. Contact - Email, phone, company name, or "Non spécifié - Voir annonce"
4. Ville - Normalized city name
5. Type de contrat - Standardized contract type

**Encoding:** UTF-8 with BOM
**Delimiter:** Comma (,)
**Quote character:** Double quote (")

## Secondary Output: Metadata JSON

**Filename format:** `job_results_YYYYMMDD_HHMMSS_metadata.json`

Contains search context, statistics, and warnings.
7. compliance_checklist.md (Purpose: Legal and ethical guidelines)
markdownCopy# Compliance Checklist

## Before Each Scraping Session

- [ ] Verify robots.txt allows access to target URLs
- [ ] Confirm Terms of Service permit automated access
- [ ] Ensure rate limiting is configured (minimum 2 seconds between requests)
- [ ] Verify no authentication bypass is required
- [ ] Confirm no personal data storage beyond session scope

## During Scraping

- [ ] Respect all robots.txt directives
- [ ] Implement exponential backoff on errors
- [ ] Use appropriate User-Agent identification
- [ ] Log all access attempts

## After Scraping

- [ ] Include data source attribution in output
- [ ] Add disclaimer about verification recommendation
- [ ] Clear session data unless explicitly saved by user
- [ ] Review logs for any compliance violations
8. error_handling.md (Purpose: Error scenarios and responses)
markdownCopy# Error Handling Specifications

## HTTP Errors

**403 Forbidden:**
- Immediately cease requests to domain
- Log: "Access denied by {domain}"
- Continue with other sources
- Report in metadata

**429 Too Many Requests:**
- Apply exponential backoff (double delay)
- Maximum 3 retry attempts
- If still failing, skip source
- Report in metadata

**404 Not Found:**
- Log specific URL
- Continue processing other listings
- Do not include in results

## Parsing Errors

**Missing Required Field:**
- Log which field is missing
- If >1 field missing: exclude listing
- If 1 field missing (except contact): include with "Non spécifié"

**Invalid Data Format:**
- Attempt type coercion
- If fails: log and exclude listing
- Report number of excluded listings in metadata

## Network Errors

**Timeout:**
- Retry up to 3 times with exponential backoff
- If still failing: skip source
- Set timeout at 30 seconds

**Connection Error:**
- Retry once after 5 seconds
- If fails: skip source
- Report in metadata
VALIDATION STEPS:
Step 1: Configuration File Validation

Verify all 8 configuration files are present in the project directory
Run JSON/YAML syntax validators on configuration files
Confirm schema validation passes for user_criteria_schema.json
Check that scraping_config.yaml contains at least 3 job site configurations

Step 2: Compliance Verification

Manually check robots.txt for each configured job site
Verify rate_limit_seconds is set to minimum 2 for all sites
Confirm no authentication-required sites are in default configuration
Review compliance_checklist.md is complete and comprehensive

Step 3: Test with Minimal Criteria
Execute the agent with this test input:
jsonCopy{
  "keywords": ["stage développeur"],
  "locations": ["Paris"],
  "max_results": 10
}
Expected behavior:

Agent requests no additional criteria (sufficient specificity)
Agent queries only configured job sites
Agent returns exactly 10 or fewer results
Output CSV has correct headers and structure
Metadata JSON is generated with search statistics

Step 4: Test Error Handling

Temporarily add an invalid job site to scraping_config.yaml
Verify agent logs the error and continues with valid sites
Verify metadata JSON reports the failed source
Verify at least one valid site still returns results

Step 5: Test Edge Cases

Submit criteria with special characters: "développeur C++"
Submit criteria with accents: "ingénieur qualité"
Submit very broad criteria (e.g., just "emploi") - agent must request clarification
Submit criteria with zero matches - agent must report zero results gracefully

Step 6: Validate Output Format

Open generated CSV in Excel/LibreOffice - confirm proper encoding (no garbled characters)
Verify all URLs are clickable and valid
Verify no duplicate entries exist
Verify contract types use only allowed values
Verify city names are consistently formatted

Step 7: Performance Validation

Time a search with max_results=50
Expected completion time: 2-5 minutes (depending on sources)
If faster: verify rate limiting is active
If slower: check for excessive retries or unoptimized parsing

COMMON PITFALLS TO AVOID:
Pitfall 1: Ignoring robots.txt

Why it occurs: Developer focuses on "getting it working" and skips compliance checks
Consequence: Legal liability, IP bans, ethical violations
Prevention: Make robots.txt check a hard requirement in code - scraper must not proceed without verification
Detection: No robots.txt parsing logs in output

Pitfall 2: Hardcoding site selectors

Why it occurs: Quickest way to get initial results
Consequence: Breaks when sites update, requires code changes instead of config updates
Prevention: Enforce selector configuration file usage, fail if selector config missing
Detection: CSS selectors or XPath expressions in Python code files

Pitfall 3: Insufficient rate limiting

Why it occurs: Desire for faster results, impatience
Consequence: IP bans, degraded performance for site, ethical concerns
Prevention: Set minimum 2-second delay as unmodifiable constant
Detection: Completion times suspiciously fast (<1 second per site)

Pitfall 4: Vague user criteria acceptance

Why it occurs: Agent tries to be "helpful" by making assumptions
Consequence: Irrelevant results, wasted processing, user frustration
Prevention: Require minimum 2 specific criteria (keyword + location), reject vague input
Detection: Agent accepts input like "looking for work" without requesting clarification

Pitfall 5: Inadequate error handling

Why it occurs: Testing only with working scenarios
Consequence: Agent crashes on first error, no results when one site fails
Prevention: Implement try-except blocks around each site scraper, continue on failure
Detection: Single site failure causes complete program termination

Pitfall 6: Missing field validation

Why it occurs: Assuming source data is always well-formatted
Consequence: Invalid URLs, empty job titles, malformed output
Prevention: Validate each extracted field against expected format before inclusion
Detection: Output CSV contains empty fields or obviously invalid data (URLs without http://)

Pitfall 7: No duplicate detection

Why it occurs: Oversight in design phase
Consequence: Same job appears multiple times from different sources
Prevention: Implement fuzzy matching on (title + company + location) before adding to results
Detection: Manual inspection reveals identical jobs with same URL or very similar titles

Pitfall 8: Synchronous scraping only

Why it occurs: Simpler to implement initially
Consequence: Very slow execution (serial processing of sites)
Prevention: Use async requests or thread pools for parallel site querying
Detection: Total execution time equals sum of individual site times (no parallelization)

Pitfall 9: Unclear output provenance

Why it occurs: Focus on just delivering results
Consequence: Users can't verify sources, can't report problems with specific sites
Prevention: Include metadata file with per-source statistics
Detection: Output lacks information about which sites were queried or failed

Pitfall 10: No mechanism for configuration updates

Why it occurs: Treating configuration as static
Consequence: Agent breaks when sites change, requires developer intervention
Prevention: Implement hot-reload of selector configs, version configuration files
Detection: Site structure change requires code modification rather than config update

Pitfall 11: Over-engineering the initial version

Why it occurs: Attempting to handle every possible job site and scenario
Consequence: Project never completes, becomes unmaintainable
Prevention: Start with 3-5 major French job sites, expand iteratively
Detection: Configuration includes >20 job sites before agent has successfully run once

Pitfall 12: Insufficient logging

Why it occurs: Viewing logging as optional
Consequence: Impossible to debug failures, no audit trail
Prevention: Log every HTTP request, every extraction attempt, every validation failure
Detection: Log file is empty or contains only high-level messages (no detailed operation logs)

IMPLEMENTATION CHECKLIST:
Phase 1: Project Setup

 Create project directory structure
 Initialize version control (git)
 Set up Python virtual environment (3.9+)
 Install dependencies: requests, beautifulsoup4, playwright, pandas, pyyaml, jsonschema, validators
 Create all 8 required configuration files (CLAUDE.md, CODEX.md, .cursorrules, scraping_config.yaml, user_criteria_schema.json, output_format.md, compliance_checklist.md, error_handling.md)

Phase 2: Configuration File Creation

 Write CLAUDE.md with agent purpose and core behavior
 Write CODEX.md with technical stack and architecture decisions
 Write .cursorrules with coding standards
 Create scraping_config.yaml with at least 3 job sites (Indeed.fr, Pole Emploi, Welcome to the Jungle)
 Create user_criteria_schema.json with complete validation rules
 Write output_format.md with CSV and JSON specifications
 Write compliance_checklist.md with pre/during/post-scraping checks
 Write error_handling.md with specific error scenarios and responses

Phase 3: Compliance Implementation

 Implement robots.txt parser function
 Create rate limiter class with per-domain tracking
 Implement Terms of Service checker (manual review + documentation)
 Add User-Agent string configuration
 Implement request logging with timestamps

Phase 4: Core Scraping Logic

 Create JobListing dataclass with 5 required fields
 Implement generic HTML parser with multiple fallback selectors
 Create site-specific scraper modules (one per job site)
 Implement data extraction with validation for each field
 Add field normalization (cities, contract types)
 Implement duplicate detection algorithm

Phase 5: Input/Output Handling

 Create user criteria parser with schema validation
 Implement criteria clarification prompts for vague input
 Create CSV output generator with proper encoding
 Create metadata JSON generator
 Add timestamp and source attribution to outputs

Phase 6: Error Handling

 Implement try-except blocks around each scraper
 Add exponential backoff for retries
 Create error logging system
 Implement graceful degradation (continue on single source failure)
 Add timeout handling for long-running requests

Phase 7: Testing

 Write unit tests for data extraction functions
 Create mock HTML files for testing parsers
 Test with valid minimal criteria
 Test with vague criteria (should request clarification)
 Test with invalid job site (should fail gracefully)
 Test with special characters in criteria
 Test duplicate detection with similar job titles
 Verify CSV opens correctly in Excel with proper encoding

Phase 8: Validation

 Run all validation steps from "VALIDATION STEPS" section
 Verify all 8 configuration files are present and syntactically valid
 Execute compliance checklist before test run
 Perform test search with 3 different criteria sets
 Verify output format matches specification exactly
 Check metadata JSON contains all required fields
 Confirm rate limiting is functioning (check timestamps in logs)

Phase 9: Documentation

 Write README.md with setup instructions
 Document how to add new job sites to configuration
 Create user guide for criteria specification
 Document common errors and solutions
 Add examples of successful searches

Phase 10: Deployment Preparation

 Review all configuration files for sensitive information
 Set up environment variables for any API keys
 Create requirements.txt with pinned versions
 Test installation from clean environment
 Verify all file paths are relative, not absolute
 Run final end-to-end test with fresh configuration

Phase 11: Maintenance Setup

 Create schedule for robots.txt compliance review (monthly)
 Set up monitoring for scraper success rates
 Document process for updating selectors when sites change
 Create issue template for reporting broken scrapers
 Plan for periodic dependency updates

Final Verification:

 Agent respects robots.txt (verified in logs)
 Agent implements minimum 2-second rate limiting (verified by timing)
 Agent validates all required fields (tested with incomplete data)
 Agent handles errors gracefully (tested with invalid sites)
 Agent outputs correct CSV format (opened in Excel successfully)
 Agent generates metadata JSON (verified structure)
 Agent detects duplicates (tested with known duplicates)
 Agent requests clarification for vague criteria (tested)
 All 8 configuration files are present and complete
 Documentation is sufficient for new user to run agent

</configuration_guidance>