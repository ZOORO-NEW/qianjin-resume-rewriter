---
slug: qianjin-resume-rewriter
displayName: 简历改写专家
summary: "简历改写专家 - 把职责罗列式简历改写成「业务背景→核心目标→落地动作→解决痛点→量化成果」三段式，破解 HR 反馈的'看不到解决问题的能力'"
license: MIT
name: qianjin-resume-rewriter
version: 1.0.1
author: qianjin
description: This skill should be used when the user wants to rewrite or optimize a resume/CV into the "project-narrative" format (项目背景/项目职责/项目成果 three-part structure) that demonstrates problem-solving ability — especially when HR feedback says the resume "看不到解决问题的能力/只写了职责没有成果", or when converting duty-list style resumes into 业务背景→核心目标→落地动作→解决痛点→量化成果 narratives. Also covers value quantification (价值量化), short-stint merging (短期经历合并), data consistency checks, and docx delivery. Triggers on 简历改写, 简历改写专家, 简历优化, 项目叙事, 突出解决问题能力, resume rewrite, resume rewriter, STAR resume.
category: 求职职业
platforms:
  - workbuddy
  - claude-code
  - cursor
  - windsurf
  - codex
trigger:
  - 简历改写
  - 简历改写专家
  - 简历优化
  - 项目叙事
  - 突出解决问题能力
  - 简历量化
  - 短期经历合并
  - 简历合并
  - resume rewrite
disable: false
agent_created: true
---

# 项目叙事式简历改写（Resume Project-Narrative）

把"职责罗列式"简历改写为"项目叙事式"简历，让招聘方一眼看到候选人**在 XX 业务背景下，围绕 XX 核心目标，通过 XX 落地动作，解决 XX 业务痛点，达成 XX 量化成果**的完整解题链路。

## 适用场景

- HR/猎头反馈简历"看不到解决问题的能力""只有职责没有成果"。
- 简历当前是"负责 XX、参与 XX"的职责清单式写法。
- 需要把多段短期经历合并，同时保持叙事完整（如"5 年内不超过 2 段主经历"）。
- 需要按目标 JD 强化特定能力线（整合营销/新媒体运营/产品/设计等均可复用本格式）。

## 核心格式（每段经历 = 一个项目）

```
### 时间段 公司 | 职位
*行业/业务一句话备注*

**项目名：一句话概括项目（体现 0-1 / 升级 / 重构 / 增长等性质）**

- **项目背景**：业务痛点 + 核心目标（1-2 句，说明"为什么要做这件事"）。
- **项目职责**：
  - **能力块名 1**：动作 + 解决的痛点 + 量化微成果。
  - **能力块名 2**：动作 + 量化微成果。
  - **能力块名 3**：动作 + 量化微成果。
  - **能力块名 4**：动作 + 量化微成果。
- **项目成果**：汇总性量化结果（2-3 个最硬的数字）+ 沉淀的可复用资产。
```

职责块小标题用**加粗能力短语**（如：业务诊断与品牌定位 / 整合营销与全域获客 / 新媒体矩阵与转化闭环 / 数据驱动增长 / AI 赋能与组织提效 / 团队搭建与协同），每个项目 3-4 个块，不写流水账。

## 改写工作流

1. **读取原简历**：本地 docx 用 `scripts/extract_docx_text.py <path>` 提取纯文本（离线可靠，无需打开文档）。
2. **盘点素材**：列出全部公司/时间段/职位/数字指标，标注哪些数字归属哪段经历——合并改写时**数字必须各归各主**，禁止混写。
3. **短期经历合并策略**（按需）：
   - 目标窗口（如近 5 年）主条目 ≤2 段；同业短经历合并为一个条目，标题写领域不写单一公司，副行标注各公司名与真实时间段（透明不造假）。
   - 合并条目内部拆成「项目一（A 公司）/ 项目二（B 公司）」，各自完整叙事——兼顾合并要求与解题链路展示。
   - 更强战绩的公司排前（"以 X 为主"）。
4. **逐段重写**：每段按核心格式改写。项目背景基于素材合理推断（行业共性痛点 + 该段动作反推的目标），**推断处必须在交付时提示用户核对**。
5. **价值量化**：用五锚点框架强化数字，详见 `references/format-guide.md`。
6. **数据一致性检查**：同一份简历内数字不得互相矛盾（经典错误："20 万增至 400 万，月增 50%"——20万→400万是约 20 倍）。口径不清时用"约/近"并统一口径。
7. **红线**：严禁编造公司、职位、数字；量化只能基于用户素材合理推演。删除"离职原因"类自辩内容。
8. **交付**：生成 markdown 源文件 + docx（用 tencent-local-office-edit 技能的 `create_doc` → `doc_insert_markdown` → `save_file` 流程新建文档，**不要改用户原文件**），present_files 交付，并附修改说明。

## 关键参考

- `references/format-guide.md`：完整格式模板、价值量化五锚点框架、能力块命名库、真实 Before→After 案例、数据一致性检查清单、docx 生成命令与路径坑。

## 质量自检（交付前）

- [ ] 每段经历都有"背景(痛点+目标) → 职责(动作+量化) → 成果(总数字)"三段，无遗漏。
- [ ] 每条 bullet 以强动词开头、以数字或明确结果收尾，无"负责/参与"式空话。
- [ ] 数字归属正确、全篇无矛盾；推断的背景已向用户声明需核对。
- [ ] 用户原始文件未被修改；交付 docx + markdown 双格式。
