---
layout: default
title: Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls
---

# Beyond Blind Spots: Analytic Hints for Mitigating LLM-Based Evaluation Pitfalls
**arXiv**：[2512.16272v1](https://arxiv.org/abs/2512.16272) · [PDF](https://arxiv.org/pdf/2512.16272.pdf)  
**作者**：Ora Nova Fandina, Eitan Farchi, Shmulik Froimovich, Raviv Gal, Wesam Ibraheem, Rami Katan, Alice Podolsky  

**一句话要点**：提出基于分析提示的混合方法，以缓解LLM在COBOL代码生成评估中的盲点问题

**关键词**：LLM评估, 代码生成, COBOL现代化, 混合系统, 错误检测, 提示工程

## 3 点简述
- 核心问题：LLM作为评估器在代码生成中易忽略领域特定错误，存在可靠性风险
- 方法要点：构建错误分类法并开发轻量分析检查器，动态注入提示以引导LLM重新评估
- 实验效果：混合方法将错误检测覆盖率从45%提升至94%，并提高解释质量

## 摘要（原文）

> Large Language Models are increasingly deployed as judges (LaaJ) in code generation pipelines. While attractive for scalability, LaaJs tend to overlook domain specific issues raising concerns about their reliability in critical evaluation tasks. To better understand these limitations in practice, we examine LaaJ behavior in a concrete industrial use case: legacy code modernization via COBOL code generation. In this setting, we find that even production deployed LaaJs can miss domain critical errors, revealing consistent blind spots in their evaluation capabilities.
>   To better understand these blind spots, we analyze generated COBOL programs and associated LaaJs judgments, drawing on expert knowledge to construct a preliminary taxonomy. Based on this taxonomy, we develop a lightweight analytic checker tool that flags over 30 domain specific issues observed in practice. We use its outputs as analytic hints, dynamically injecting them into the judges prompt to encourage LaaJ to revisit aspects it may have overlooked.
>   Experiments on a test set of 100 programs using four production level LaaJs show that LaaJ alone detects only about 45% of the errors present in the code (in all judges we tested), while the analytic checker alone lacks explanatory depth. When combined, the LaaJ+Hints configuration achieves up to 94% coverage (for the best performing judge and injection prompt) and produces qualitatively richer, more accurate explanations, demonstrating that analytic-LLM hybrids can substantially enhance evaluation reliability in deployed pipelines. We release the dataset and all used prompts.

