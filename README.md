# api-security-vijay-kumar-panga

## Consequences of Exposing API Keys on GitHub

- **Financial damage** – Attackers exploit leaked keys to consume paid services, leading to massive unexpected bills.
- **Data breaches** – Keys granting access to databases or storage can result in stolen or deleted data.
- **Automated exploitation** – Bots actively scan GitHub for secrets and exploit them within minutes.
- **Mitigation** – Use environment variables, secret managers (e.g., AWS Secrets Manager), `.gitignore`, and secret scanning tools.

## Why Logging City Names May Violate Privacy Policies

- **PII regulations** – Under GDPR/CCPA, city-level location data combined with other fields can identify individuals.
- **Data minimization** – Privacy frameworks require storing only what's strictly necessary for the system to function.
- **Breach liability** – PII in logs increases legal exposure if logs are compromised.