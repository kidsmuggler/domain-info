import whois

def info(domain_name):
    data = whois.whois(domain_name)
    return data
domain_name = input(f"Enter URL :-  ")
        
def x(data):
    print(f"""\n
Domain Name: {data.domain_name}
Registrar WHOIS Server: {data.whois_server}
Registrar URL: {data.registrar_url}
Updated Date: {data.updated_date}
Creation Date: {data.creation_date}
Expiration Date: {data.expiration_date}
Registrar: {data.registrar}
Registrar IANA ID: {data.registrar_iana_id}
Domain Status: {data.status}
Registrant Name: {data.name}
Registrant Organization: {data.org}
Registrant Country: {data.country}
Registrant City: {data.city}
Registrant Street: {data.address}
Registrant Province: {data.state}
Registrant Zip Code: {data.zipcode}
Registrant Phone: {data.phone}
Registrant Email: {data.email}
Name Servers: {data.name_servers}
Registrar Abuse Email: {data.abuse_email}
Registrar Abuse Phone: {data.abuse_phone}
\n""")

if __name__ == "__main__":
    data = info(domain_name)
    x(data)
