import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


class TacomachiAgent:

    def __init__(self):
        self.cf_api_token = os.getenv("CLOUDFLARE_API_TOKEN", "")
        self.cf_account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
        self.cf_zone_id = os.getenv("CLOUDFLARE_ZONE_ID", "")

    def load_skill(self):
        try:
            with open("skill.md", "r", encoding="utf-8") as f:
                skill = f.read()
                print("[INFO] skill.md loaded:", len(skill), "chars")
        except FileNotFoundError:
            print("[WARN] skill.md not found")

    def fetch_logs(self):
        print("[INFO] Fetch logs (Cloudflare) – placeholder")
        return []

    def detect_anomaly(self, logs):
        print("[INFO] Detect anomaly – placeholder")
        return []

    def send_alert(self, anomalies):
        if anomalies:
            print("[ALERT] anomaly detected")
        else:
            print("[INFO] no anomaly")

    def run(self):
        print("=== Tacomachi Agent Start ===")
        print("Time:", datetime.now())

        print("Token set:", bool(self.cf_api_token))
        print("Account ID set:", bool(self.cf_account_id))
        print("Zone ID set:", bool(self.cf_zone_id))

        self.load_skill()

        logs = self.fetch_logs()
        anomalies = self.detect_anomaly(logs)
        self.send_alert(anomalies)

        print("=== Agent End ===")


# ===== Moltbook Owner Email Setup =====
def setup_moltbook_owner_email():
    API_KEY = os.getenv("MOLTBOOK_API_KEY")
    EMAIL = "admin@noobdna.com"

    url = "https://www.moltbook.com/api/v1/agents/me/setup-owner-email"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "email": EMAIL
    }

    r = requests.post(url, headers=headers, json=data)
    print("Moltbook owner email setup:", r.status_code, r.text)


if __name__ == "__main__":
    setup_moltbook_owner_email()
