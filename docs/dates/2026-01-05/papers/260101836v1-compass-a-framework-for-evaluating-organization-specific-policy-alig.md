---
layout: default
title: COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs
---

# COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs
**arXiv**：[2601.01836v1](https://arxiv.org/abs/2601.01836) · [PDF](https://arxiv.org/pdf/2601.01836.pdf)  
**作者**：Dasol Choi, DongGeon Lee, Brigitta Jesica Kartono, Helena Berndt, Taeyoun Kwon, Joonwon Jang, Haon Park, Hwanjo Yu, Minsuk Kahng  

**一句话要点**：提出COMPASS框架以评估大语言模型在组织特定政策下的对齐性

**关键词**：大语言模型评估, 组织政策对齐, 安全框架, 合规性测试, 企业应用

## 3 点简述
- 核心问题：现有安全评估仅关注通用危害，缺乏针对组织特定政策的评估方法
- 方法要点：开发COMPASS框架，基于允许列表和禁止列表政策生成查询测试合规性
- 实验或效果：在八个行业场景中测试七种模型，发现模型在处理禁止请求时失败率高达60-87%

## 摘要（原文）

> As large language models are deployed in high-stakes enterprise applications, from healthcare to finance, ensuring adherence to organization-specific policies has become essential. Yet existing safety evaluations focus exclusively on universal harms. We present COMPASS (Company/Organization Policy Alignment Assessment), the first systematic framework for evaluating whether LLMs comply with organizational allowlist and denylist policies. We apply COMPASS to eight diverse industry scenarios, generating and validating 5,920 queries that test both routine compliance and adversarial robustness through strategically designed edge cases. Evaluating seven state-of-the-art models, we uncover a fundamental asymmetry: models reliably handle legitimate requests (>95% accuracy) but catastrophically fail at enforcing prohibitions, refusing only 13-40% of adversarial denylist violations. These results demonstrate that current LLMs lack the robustness required for policy-critical deployments, establishing COMPASS as an essential evaluation framework for organizational AI safety.

