# After grill-me: check the interpretations that survived implementation

[中文](after-grill-me.zh-CN.md) · [Home](../README.md)

[Matt Pocock's grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) helps an idea become clearer through an interview. His [grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) provides a related entry point for repository work. Both remain useful on their own.

Implementation introduces more interpretations: a local instruction becomes a shared rule, an example becomes a default, or one conversation's shortcut reaches another branch. Post Grill Me makes those interpretations visible in small rounds.

## A copyable follow-up

After implementing a change, ask your agent:

```text
Use post-grill-me on this change. Show the one or two interpretations you adopted
that would most affect behavior if wrong. State the short basis and consequence.
Let me correct the scope, and keep the feature story in a recap for later.
```

In Codex, prefix the prompt with `$post-grill-me`; with the Chinese variant, use `$post-grill-me-zh`. Other clients use their own installed-skill invocation. You can also invoke it midway through work when the direction feels slightly off.

## What a useful checkpoint catches

Suppose an interview established that an export preview should handle archived items like ordinary items. During implementation, the agent applies that interpretation to a scheduled job too. Tests might accurately verify that broadened behavior, while the scope still needs a human correction.

The checkpoint should surface: “I extended the preview rule to the scheduled job. Should that rule cover both?” It should not begin a full code audit, manufacture a past interpretation, or ask the user to repeat the whole interview.

If related chats disagree, separate their branch, stage, or use case first. Keep an earlier confirmed scope unless a clear same-scope correction supersedes it. A later brainstorming message alone does not settle the version.

## Keep the pairing lightweight

- Install this skill by itself; grill-me and grilling are not dependencies.
- Ask about meaning and scope before deciding whether code needs a change.
- Save the feature background and corrected interpretation so a future teammate can recover the story.
- Use [the example record](../examples/feature-recap.md) to see the intended reading experience.

This is an independent companion, not an official extension of Matt Pocock's project.
