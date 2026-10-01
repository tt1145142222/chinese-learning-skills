# 中文学习与教学 Skills

一组用于课程练习、复习资料、持续教学和文档排版的 Codex Skills。每个 Skill 包含 `SKILL.md` 指令和其实际需要的参考、模板或辅助脚本。它们需要支持 Skill 指令的助手执行，不是独立运行的教学软件。

## 功能

| Skill | 用途 | 常见交付物 |
| --- | --- | --- |
| [caikeji-mock-exam](skills/caikeji-mock-exam/SKILL.md) | 按课程章节和考试范围制作材料科学与工程基础模拟卷 | 题目 PDF、详细答案解析 PDF |
| [math-practice-generator](skills/math-practice-generator/SKILL.md) | 根据主题或课程材料生成数理练习与试卷 | 练习 PDF、答案解析 PDF |
| [iterative-lesson-cycle](skills/iterative-lesson-cycle/SKILL.md) | 串联上课、练习、订正与复测，持续维护课程档案 | 教案、练习、学情与迭代日志 |
| [maogai-review-doc-builder](skills/maogai-review-doc-builder/SKILL.md) | 根据毛概/毛中特课程材料整理章节复习文档 | 题目练习版 DOCX、答案解析版 DOCX |
| [latex-polished-doc-builder](skills/latex-polished-doc-builder/SKILL.md) | 将笔记、公式和混合文档重排为语义化 LaTeX | LaTeX 源文件、可打印 PDF |

选择一个主要工作流，按实际需要使用配套文档能力。题目与答案分开保存，使用者明确的范围和交付要求优先。

## 安装

下载仓库 ZIP 并解压，或从实际仓库地址克隆。进入包含本 README 和 `skills/` 的根目录。在 PowerShell 中可安装一个 Skill：

```powershell
$skillName = 'math-practice-generator'
$skillRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path $env:USERPROFILE '.codex\skills'
}
$sourceSkill = Join-Path (Join-Path (Get-Location).Path 'skills') $skillName
$targetSkill = Join-Path $skillRoot $skillName
if (-not (Test-Path -LiteralPath $sourceSkill -PathType Container)) {
    throw '请先切换到仓库根目录。'
}
if (Test-Path -LiteralPath $targetSkill) {
    throw '目标 skill 已存在。先比较版本并自行备份，避免覆盖已有规则或数据。'
}
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath $sourceSkill -Destination $targetSkill -Recurse
```

将 `$skillName` 改为表中的名称即可安装其他项目。保留整个 Skill 文件夹，不能只复制 `SKILL.md`。开始新会话后确认 Skill 出现在可用列表中；未自动发现时，在对话中指定它的完整 `SKILL.md` 路径，请助手读取后执行。

## 调用示例

以下内容是给助手的对话文字，`$技能名` 不是终端命令。目录、章节和时间预算应换成自己的要求。

```text
用 $math-practice-generator，围绕闭区间最值生成 30 分钟的原创练习。
题目卷与解析卷分开，输出到当前课程项目的 outputs 目录。
```

```text
用 $caikeji-mock-exam，根据当前 materials 目录中的已授权材料，
只覆盖第二章及 exam-scope.md 中的范围，生成题目卷和答案解析卷。
```

```text
用 $iterative-lesson-cycle，在当前 course 项目初始化持续教学记录。
只建立课程档案和匿名学习者模型；缺失的课堂证据标为缺失。
```

```text
用 $maogai-review-doc-builder，根据我提供的课程范围和已授权材料，
制作分章节的题目练习版和答案解析版 Word 文档。
```

```text
用 $latex-polished-doc-builder，把 examples/math-practice/topics.md
重排为可打印的中文 LaTeX/PDF，保留原题和符号，输出到当前项目。
```

更多新编或虚构输入见 [examples/README.md](examples/README.md)。示例不包含教材、真实学生数据或论文附件。

## 依赖

| 功能 | 依赖及限制 |
| --- | --- |
| 读取 Skill 与组织教学内容 | 支持 Skill 指令的助手、对所选项目的读写权限 |
| 材科基/数理练习 PDF | XeLaTeX 或 LuaLaTeX、`ctex` 与模板所需 TeX 宏包、中文字体、PDF 页面检查能力 |
| 持续教学 | 课程证据由使用者提供；输出格式需要的 Word/PDF 等能力按需准备 |
| 毛概 Word | 可用的 `documents:documents` 能力；有 PDF 来源时按需使用 `pdf:pdf`。两个捆绑清点/结构检查脚本只用 Python 标准库，不能独立代替文档生成 |
| LaTeX 文档检查 | Python 3；页面预览脚本需要 Pillow 和 Poppler 的 `pdftoppm`；日志检查脚本只用标准库 |

插件、TeX 发行版、字体、PDF 渲染程序及 Python 包不随仓库打包。可在自己的项目虚拟环境中安装 Pillow：`python -m pip install Pillow`。仅阅读指令无需安装。

中文 LaTeX 示例使用 `ctex`、`amsmath`、`amssymb`、`mathtools`、`bm`、`geometry`、`tcolorbox`、`fancyhdr`、`titlesec`、`enumitem`、`needspace`、`lastpage` 等宏包。Windows 字体示例需要相应字体，其他系统应选择本机可用的字体配置。

辅助脚本应在对应 Skill 目录运行，例如：

```powershell
python scripts/source_inventory.py '<自己的课程资料目录>'
python scripts/qa_review_docs.py --practice '<练习版.docx>' --answers '<解析版.docx>' --chapters 3
```

本包不包含水印功能、视频制作/投稿功能、运行历史、账户绑定或系统定时任务配置。课程材料也不随包提供。PDF 生成不可用时应据实交付源文件并说明未编译；Word 插件或渲染不可用时应说明相应限制，不能声称已完成未执行的步骤。

## 验证与隐私

五项 Skill 结构、捆绑 Python 语法、YAML 与文件引用已检查。虚构 DOCX 结构检查、数理练习模板的 XeLaTeX 编译、日志检查及 PDF 页面渲染已在本机通过。完整课程资料提取、AI 出题准确性、持续教学闭环及 Word 全流程视觉检查尚未端到端验证，也没有承诺其他环境开箱即用。检查范围见 [VALIDATION.md](VALIDATION.md)。

使用者自行提供有权使用的教材、课件和题库。真实学情、学生作答与身份保存在自己的课程项目中，不应上传公开仓库。不要附加登录信息、发布回执、教材扫描件、付费论文或私有素材。

## 许可与来源

尚未选择开放许可证，公开可见不等于获得复制、修改或再分发的额外许可，详见 [LICENSE-STATUS.md](LICENSE-STATUS.md)。第三方工具和使用者提供材料的权利单独判断。

本包公开范围为上述五项本地定制 Skill，第三方/内置 Skill 未打包。依赖边界见 [THIRD-PARTY.md](THIRD-PARTY.md)，副本调整与文件摘要见 [EXPORT-MANIFEST.json](EXPORT-MANIFEST.json)。
