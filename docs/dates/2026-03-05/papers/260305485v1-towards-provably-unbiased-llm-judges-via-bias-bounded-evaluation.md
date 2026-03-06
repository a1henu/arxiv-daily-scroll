---
layout: default
title: Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation
---

# Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation
**arXiv**：[2603.05485v1](https://arxiv.org/abs/2603.05485) · [PDF](https://arxiv.org/pdf/2603.05485.pdf)  
**作者**：Benjamin Feuer, Lucas Rosenblatt, Oussama Elachqar  

**一句话要点**：提出平均偏置有界性框架以保障LLM评判者在未知偏置下的可靠反馈

**关键词**：LLM评判者, 偏置有界性, 自主AI系统, 形式化保证, 反馈循环

## 3 点简述
- 核心问题：LLM评判者在自主AI系统中存在未知或对抗性偏置，缺乏强保证机制。
- 方法要点：引入平均偏置有界性算法框架，形式化保证可测量偏置对伤害/影响的减少。
- 实验或效果：在Arena-Hard-Auto上评估，实现偏置有界保证，同时保持61-99%与原排名的相关性。

## 摘要（原文）

> As AI models progress beyond simple chatbots into more complex workflows, we draw ever closer to the event horizon beyond which AI systems will be utilized in autonomous, self-maintaining feedback loops. Any autonomous AI system will depend on automated, verifiable rewards and feedback; in settings where ground truth is sparse or non-deterministic, one practical source of such rewards is an LLM-as-a-Judge. Although LLM judges continue to improve, the literature has yet to introduce systems capable of enforcing standards with strong guarantees, particularly when bias vectors are unknown or adversarially discovered. To remedy this issue, we propose average bias-boundedness (A-BB), an algorithmic framework which formally guarantees reductions of harm/impact as a result of any measurable bias in an LLM judge. Evaluating on Arena-Hard-Auto with four LLM judges, we achieve (tau=0.5, delta=0.01) bias-bounded guarantees while retaining 61-99% correlation with original rankings across formatting and schematic bias settings, with most judge-bias combinations exceeding 80%. The code to reproduce our findings is available at https://github.com/penfever/bias-bounded-evaluation.

