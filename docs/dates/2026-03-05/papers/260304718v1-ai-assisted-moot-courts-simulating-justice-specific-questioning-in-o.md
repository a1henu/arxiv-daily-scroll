---
layout: default
title: AI-Assisted Moot Courts: Simulating Justice-Specific Questioning in Oral Arguments
---

# AI-Assisted Moot Courts: Simulating Justice-Specific Questioning in Oral Arguments
**arXiv**：[2603.04718v1](https://arxiv.org/abs/2603.04718) · [PDF](https://arxiv.org/pdf/2603.04718.pdf)  
**作者**：Kylie Zhang, Nimra Nadeem, Lucia Zheng, Dominik Stammbach, Peter Henderson  

**一句话要点**：提出AI辅助模拟法庭以模拟法官特定提问，用于口头辩论训练

**关键词**：AI辅助模拟法庭, 口头辩论模拟, 法官特定提问, 双层评估框架, 法律AI应用

## 3 点简述
- 核心问题：AI能否有效模拟法官在口头辩论中的特定提问，以提升模拟法庭训练效果
- 方法要点：基于美国最高法院口头辩论转录本数据集，构建提示式和代理式模拟器，并引入双层评估框架
- 实验或效果：模拟问题在人类标注者中常被视为真实，能高召回实质性法律问题，但存在提问类型多样性和谄媚性不足

## 摘要（原文）

> In oral arguments, judges probe attorneys with questions about the factual record, legal claims, and the strength of their arguments. To prepare for this questioning, both law schools and practicing attorneys rely on moot courts: practice simulations of appellate hearings. Leveraging a dataset of U.S. Supreme Court oral argument transcripts, we examine whether AI models can effectively simulate justice-specific questioning for moot court-style training. Evaluating oral argument simulation is challenging because there is no single correct question for any given turn. Instead, effective questioning should reflect a combination of desirable qualities, such as anticipating substantive legal issues, detecting logical weaknesses, and maintaining an appropriately adversarial tone. We introduce a two-layer evaluation framework that assesses both the realism and pedagogical usefulness of simulated questions using complementary proxy metrics. We construct and evaluate both prompt-based and agentic oral argument simulators. We find that simulated questions are often perceived as realistic by human annotators and achieve high recall of ground truth substantive legal issues. However, models still face substantial shortcomings, including low diversity in question types and sycophancy. Importantly, these shortcomings would remain undetected under naive evaluation approaches.

