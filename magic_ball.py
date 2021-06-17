@slash.slash(name="magic-ashball", guild_ids=guild_ids())
async def _magic_ashball(ctx):
    choices = [
        "Uhhhh so like Yeah! You got this!",
        "Nope the end is near",
        "That's definitely a possibility",
        "Dont get your hopes up",
        "Oof, yeah that's not happening",
        "I'll get back to you",
        "For sure",
        "Absolutely"
    ]
    response = random.choice(choices)
    await ctx.send(response)
