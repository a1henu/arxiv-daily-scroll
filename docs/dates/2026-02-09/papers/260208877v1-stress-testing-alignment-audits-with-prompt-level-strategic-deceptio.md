---
layout: default
title: Stress-Testing Alignment Audits With Prompt-Level Strategic Deception
---

# Stress-Testing Alignment Audits With Prompt-Level Strategic Deception
**arXiv**：[2602.08877v1](https://arxiv.org/abs/2602.08877) · [PDF](https://arxiv.org/pdf/2602.08877.pdf)  
**作者**：Oliver Daniels, Perusha Moodley, Ben Marlin, David Lindner  

**一句话要点**：提出自动红队管道以压力测试对齐审计方法，揭示策略性欺骗漏洞

**关键词**：对齐审计, 策略性欺骗, 红队测试, 白盒审计, 黑盒审计, 系统提示

## 3 点简述
- 核心问题：现有对齐审计方法未系统测试对抗策略性欺骗的鲁棒性
- 方法要点：构建自动红队管道，生成针对白盒和黑盒审计方法的欺骗性系统提示
- 实验或效果：在秘密保持模型上测试多种审计方法，发现欺骗导致错误猜测

## 摘要（原文）

> Alignment audits aim to robustly identify hidden goals from strategic, situationally aware misaligned models. Despite this threat model, existing auditing methods have not been systematically stress-tested against deception strategies. We address this gap, implementing an automatic red-team pipeline that generates deception strategies (in the form of system prompts) tailored to specific white-box and black-box auditing methods. Stress-testing assistant prefills, user persona sampling, sparse autoencoders, and token embedding similarity methods against secret-keeping model organisms, our automatic red-team pipeline finds prompts that deceive both the black-box and white-box methods into confident, incorrect guesses. Our results provide the first documented evidence of activation-based strategic deception, and suggest that current black-box and white-box methods would not be robust to a sufficiently capable misaligned model.

