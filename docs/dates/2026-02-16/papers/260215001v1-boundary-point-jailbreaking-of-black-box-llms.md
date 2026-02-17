---
layout: default
title: Boundary Point Jailbreaking of Black-Box LLMs
---

# Boundary Point Jailbreaking of Black-Box LLMs
**arXiv**：[2602.15001v1](https://arxiv.org/abs/2602.15001) · [PDF](https://arxiv.org/pdf/2602.15001.pdf)  
**作者**：Xander Davies, Giorgi Giglemiani, Edmund Lau, Eric Winsor, Geoffrey Irving, Yarin Gal  

**一句话要点**：提出边界点越狱攻击以规避黑盒大语言模型的强分类器防御

**关键词**：越狱攻击, 黑盒优化, 分类器防御, 边界点选择, 课程学习, 大语言模型安全

## 3 点简述
- 核心问题：现有越狱攻击依赖白盒/灰盒假设或现有库，难以对抗强分类器防御。
- 方法要点：基于单比特反馈，通过课程学习和边界点选择优化攻击，实现全黑盒自动化。
- 实验或效果：成功攻击宪法分类器和GPT-5输入分类器，无需人类攻击种子。

## 摘要（原文）

> Frontier LLMs are safeguarded against attempts to extract harmful information via adversarial prompts known as "jailbreaks". Recently, defenders have developed classifier-based systems that have survived thousands of hours of human red teaming. We introduce Boundary Point Jailbreaking (BPJ), a new class of automated jailbreak attacks that evade the strongest industry-deployed safeguards. Unlike previous attacks that rely on white/grey-box assumptions (such as classifier scores or gradients) or libraries of existing jailbreaks, BPJ is fully black-box and uses only a single bit of information per query: whether or not the classifier flags the interaction. To achieve this, BPJ addresses the core difficulty in optimising attacks against robust real-world defences: evaluating whether a proposed modification to an attack is an improvement. Instead of directly trying to learn an attack for a target harmful string, BPJ converts the string into a curriculum of intermediate attack targets and then actively selects evaluation points that best detect small changes in attack strength ("boundary points"). We believe BPJ is the first fully automated attack algorithm that succeeds in developing universal jailbreaks against Constitutional Classifiers, as well as the first automated attack algorithm that succeeds against GPT-5's input classifier without relying on human attack seeds. BPJ is difficult to defend against in individual interactions but incurs many flags during optimisation, suggesting that effective defence requires supplementing single-interaction methods with batch-level monitoring.

