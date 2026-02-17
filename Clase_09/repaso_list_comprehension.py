list_ip = ["123.02.02.159", "100.01.02.15", "200.100.150.01"]

# ip 123 ->Congo
# ip 100 -> USA
# ip 200 -> Tailandia

list_tailandia = [ ip.find("200", 0, 3) == 0 for ip in list_ip ]

print(f"Is there any visitor from Tailandia {any(list_tailandia)}")
