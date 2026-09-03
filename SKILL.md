---
slug: qianjin-resume-rewriter
displayName: 简历改写专家
summary: "简历改写专家 - 围绕目标岗位，用「明确目标→筛选经历→包装经历→对齐工作结果→突出解决问题能力→格式优化」六步法，把职责罗列式简历改写成让 HR 一眼看到解题链路的简历。"
license: MIT
name: qianjin-resume-rewriter
version: 1.1.0
author: qianjin
description: This skill rewrites/optimizes a resume/CV around a TARGET role using a six-step method — clarify goal → filter experiences → package experiences (project-narrative) → align results to the JD → highlight problem-solving → polish format. It turns duty-list resumes ("负责 XX、参与 XX") into "business background → core goal → actions → pain solved → quantified results" narratives that make the candidate's problem-solving ability visible. Use when HR feedback says the resume "看不到解决问题的能力/只有职责没有成果", or for 简历改写/简历优化/项目叙事/突出解决问题能力/对齐JD/筛选经历/格式优化/resume rewrite/STAR resume. Also covers value quantification (价值量化五锚点), short-stint merging, data-consistency checks, and docx delivery.
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
  - 明确目标
  - 筛选经历
  - 对齐JD
  - 简历包装
  - 格式优化
  - resume rewrite
  - resume rewriter
  - resume optimization
disable: false
agent_created: true
---

# 简历改写专家（Resume Optimization Expert）

把"职责罗列式"简历，围绕**目标岗位**，改写成让招聘方一眼看到
**「在 XX 业务背景下，围绕 XX 核心目标，用 XX 落地动作，解决 XX 业务痛点，达成 XX 量化成果」**完整解题链路的简历。

## 适用场景

- HR/猎头反馈"看不到解决问题的能力""只有职责没有成果"。
- 简历当前是"负责 XX、参与 XX"的职责清单式写法。
- 经历很多但与目标岗位不相关，需要筛选聚焦。
- 需要按目标 JD 强化特定能力线、合并短期经历，或做 docx 交付。

## 简历优化六步法（核心流程）

### 1. 明确目标（Clarify Goal）
没有目标的简历优化是无效优化——先锁定"打谁"，再动手。
- **目标岗位 + 行业 + 意向公司/层级**（如"互联网大厂 高级运营""传统企业 品牌总监"）。
- 若有 JD：提取**硬性要求（年限/学历/硬技能/行业）+ 软性要求（能力特质）+ 高频关键词**。
- 若无 JD：基于目标岗位共性，推导招聘方最关心的 3-4 条能力线，作为改写主线。
- 输出：一句话"目标画像"——这份简历要证明"我能胜任 XX 岗的 XX 能力"，后续每段都回扣它。

### 2. 筛选经历（Filter Experiences）
从用户全量经历中按目标画像做减法：
- **强相关 + 有硬数字** → 重点展开、前置。
- **弱相关 + 可迁移能力** → 保留但精简。
- **无关 / 超过 10 年** → 一笔带过或删除。
- **战绩最硬** → 排前（"以 X 公司为主"）。
- 合并策略：近 5 年主条目 ≤2 段；同业短经历合并为一条（标题写领域、副行标注真实公司+时间段），内部拆「项目一（A 公司）/ 项目二（B 公司）」各自完整叙事。

### 3. 包装经历（Package — 项目叙事式）
每段经历 = 一个项目，采用「背景→职责→成果」三段式（模板见 `references/format-guide.md`）：
- **项目背景**：业务痛点 + 核心目标（1-2 句，说明"为什么要做这件事"）。
- **项目职责**：3-4 个**加粗能力块**（动作 + 解决的痛点 + 量化微成果）。
- **项目成果**：2-3 个最硬的总数字 + 可复用资产。
- 背景可基于素材合理推断，但**推断处必须向用户声明需核对**（不造假）。

### 4. 对齐工作结果（Align to JD）
让每段经历都"长在点上"，而不是"写了很多却没打中"：
- 把 JD 关键词/能力要求，自然融入对应项目的能力块标题与成果（同义表述，不堆砌）。
- 同一能力跨多项目时，用递进写法（"0-1 → 规模化 → 体系化"）体现成长。
- 成果优先呈现 JD 最看重的那类价值（目标偏增长→突出 GMV/获客；偏效率→突出降本/周期缩短）。

### 5. 突出解决问题的能力（Highlight Problem-Solving）
这是简历的灵魂，贯穿全程：
- 每条 bullet 以**强动词**开头、以**数字/明确结果**收尾，杜绝"负责/参与"空话。
- 用「问题→动作→结果」结构，而非「职责→职责」：先点痛点，再写你怎么做，最后给结果。
- 用价值量化五锚点强化（钱 > 增长 > 效率 > 规模 > 获客转化，详见格式指南）。

### 6. 格式优化（Format Polish）
- **ATS 友好**：纯文本可解析，避免图片/表格/文本框/复杂分栏；关键词与 JD 同义表述。
- **可扫读**：每段 3-4 个加粗能力块小标题，一屏可见"痛点 + 成果"。
- **分层呈现**：个人信息 → 摘要/核心能力 → 经历（重点前置）→ 教育/其他。
- **一致性**：数字口径统一、时间线连续、公司名/职位前后一致；不写离职原因与自我评价空话。

## 改写工作流（执行细节）

1. **读取原简历**：本地 docx 用 `scripts/extract_docx_text.py <path>` 提取纯文本（离线可靠，无需打开文档）。
2. **盘点素材**：列出全部公司/时间段/职位/数字指标，标注数字归属——合并改写时**数字必须各归各主**，禁止混写。
3. **六步法改写**：按上面六步逐段重写（明确目标 → 筛选 → 包装 → 对齐 → 突出 → 格式）。
4. **价值量化**：用五锚点框架强化数字，详见 `references/format-guide.md`。
5. **数据一致性检查**：同一份简历内数字不得互相矛盾（如"20 万→400 万"是约 20 倍，不能同时写"提升 50%"）；口径不清用"约/近"并统一。
6. **红线**：严禁编造公司、职位、数字；量化只能基于用户素材合理推演；删除"离职原因"类自辩；**绝不改用户原文件**。
7. **交付**：生成 markdown 源文件 + docx（用 tencent-local-office-edit 的 `create_doc` → `doc_insert_markdown` → `save_file` 新建文档），present_files 交付，并附修改说明。

## 关键参考

- `references/format-guide.md`：明确目标与 JD 拆解法、经历筛选标准、JD-结果对齐表、价值量化五锚点框架、能力块命名库、真实 Before→After 案例、ATS 与格式优化清单、docx 生成命令与路径坑。

## 质量自检（交付前）

- [ ] 已明确目标岗位与能力优先级（第 1 步有据，非凭空）。
- [ ] 经历已按目标筛选聚焦，无关内容已删减/精简。
- [ ] 每段经历都有"背景(痛点+目标) → 职责(动作+量化) → 成果(总数字)"三段。
- [ ] JD 关键词已自然落到能力块/成果；成果方向对齐目标偏好。
- [ ] 每条 bullet 强动词开头、数字收尾，突出解题而非罗列职责。
- [ ] 格式 ATS 友好、可扫读、数字一致；推断的背景已向用户声明核对。
- [ ] 用户原始文件未被修改；交付 docx + markdown 双格式。
