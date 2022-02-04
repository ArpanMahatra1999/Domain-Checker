import whois


def check_domain(domain):
    checked_domain = whois.whois(domain)
    checked_domain_name = checked_domain.domain_name
    return checked_domain_name


print(check_domain("gatsbyjs."))
