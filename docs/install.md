# Installation / 安装

[English home](../README.md) · [中文首页](../README.zh-CN.md)

## Skills CLI

The [upstream CLI](https://github.com/vercel-labs/skills) currently requires Node.js 22.20 or later. Choose either complete skill:

```bash
npx skills add Gsnow0123/post-grill-me --skill post-grill-me
npx skills add Gsnow0123/post-grill-me --skill post-grill-me-zh
```

Run **one** command for your preferred instruction language. The CLI prompts for the target agent; project installation is the default, and `-g` requests a user-level installation. Consult the [upstream command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for available options.

中文：选择一种指令语言执行对应命令即可，CLI 会让你选择目标 agent。默认安装到项目，加 `-g` 为用户级安装。两版的流程相同，回答语言跟随实际对话。

## Manual Codex installation / 手动安装

[Official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) describes repository-local `.agents/skills` and user-level `~/.agents/skills` directories. Copy the complete folder, including its `references`, `agents`, and `LICENSE` files.

From a cloned checkout, for a project-local English install:

```bash
mkdir -p /path/to/your-project/.agents/skills
cp -R skills/post-grill-me /path/to/your-project/.agents/skills/
```

Or in PowerShell, with your intended project path:

```powershell
$skillDestination = Join-Path $projectPath '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillDestination | Out-Null
Copy-Item -LiteralPath '.\skills\post-grill-me' -Destination $skillDestination -Recurse
```

For Chinese instructions, replace the source folder with `skills/post-grill-me-zh`. For user-wide use, target your user `.agents/skills` directory. Check for an existing folder with the same name before copying; intentionally replace it or use a separate project install rather than nesting or accidentally overwriting it.

中文：复制完整 skill 文件夹。中文版将来源改成 `skills/post-grill-me-zh`。用户级安装使用自己的 `.agents/skills` 目录；复制前检查同名目录，避免误覆盖或套娃目录。如果客户端未发现新 skill，按其文档刷新或重启。

## Release ZIPs / 发布包

The [releases page](https://github.com/Gsnow0123/post-grill-me/releases) provides a ZIP for each language. Each archive contains one complete skill directory and its MIT license. Extract it and copy that directory to your client's skill location.

发布页提供两种语言的独立压缩包，解压后将完整目录放入客户端的 skill 位置即可。无需下载另一个配套 skill。

## Output directory / 保存位置

Place `.post-grill-me.json` at your project root if you want a stable output directory:

```json
{
  "artifact_root": "docs/feature-recaps"
}
```

The path is relative to this config file. The [example config](../.post-grill-me.example.json) uses no personal path. This repository ignores the actual local config to avoid publishing machine-specific settings. The skill asks before creating a missing directory and respects normal permissions.

中文：想固定保存位置，可使用上述项目配置。相对路径基于配置文件，目录不存在时先确认再创建；权限问题不会触发偷偷改存别处。实际本地配置不纳入本仓库版本控制。
