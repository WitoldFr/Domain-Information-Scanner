import whois
import dns.resolver
import requests

def get_whois_info(domain):
   
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "name_servers": w.name_servers
        }
    except Exception as e:
        print(f"Błąd w pobieraniu informacji WHOIS dla {domain}: {e}")
        return None

def get_dns_info(domain):
    
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [str(answer) for answer in answers]
    except Exception as e:
        print(f"Błąd w pobieraniu informacji DNS dla {domain}: {e}")
        return []

def check_ssl(domain):
    
    try:
        response = requests.get(f'https://{domain}', timeout=5)
        return response.url, response.status_code
    except Exception as e:
        print(f"Błąd przy sprawdzaniu SSL dla {domain}: {e}")
        return None, None

def main():
    domain = input("Podaj nazwę domeny (np. example.com): ")
    
    
    whois_info = get_whois_info(domain)
    if whois_info:
        print("\nInformacje WHOIS:")
        for key, value in whois_info.items():
            print(f"{key}: {value}")

    
    dns_info = get_dns_info(domain)
    if dns_info:
        print("\nInformacje DNS:")
        print("Adresy IP:", dns_info)

    
    ssl_info = check_ssl(domain)
    if ssl_info[0]:
        print("\nInformacje SSL:")
        print(f"URL: {ssl_info[0]}, Status kodu: {ssl_info[1]}")

if __name__ == "__main__":
    main()
