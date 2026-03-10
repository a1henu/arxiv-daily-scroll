---
layout: default
title: The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs
---

# The Struggle Between Continuation and Refusal: A Mechanistic Analysis of the Continuation-Triggered Jailbreak in LLMs
**arXiv**：[2603.08234v1](https://arxiv.org/abs/2603.08234) · [PDF](https://arxiv.org/pdf/2603.08234.pdf)  
**作者**：Yonghong Deng, Zhen Yang, Ping Jian, Xinyue Zhang, Zhongbin Guo, Chengzhi Li  

**一句话要点**：通过注意力头机制分析揭示LLM中延续触发越狱的竞争机制

**关键词**：大语言模型安全, 越狱攻击, 机制可解释性, 注意力头分析, 安全对齐

## 3 点简述
- 研究LLM延续触发越狱现象，即指令后缀重定位显著提升越狱成功率
- 采用注意力头层面的因果干预和激活缩放，分析延续驱动与安全防御的竞争
- 识别安全关键注意力头，发现不同模型架构中安全头功能与行为差异

## 摘要（原文）

> With the rapid advancement of large language models (LLMs), the safety of LLMs has become a critical concern. Despite significant efforts in safety alignment, current LLMs remain vulnerable to jailbreaking attacks. However, the root causes of such vulnerabilities are still poorly understood, necessitating a rigorous investigation into jailbreak mechanisms across both academic and industrial communities. In this work, we focus on a continuation-triggered jailbreak phenomenon, whereby simply relocating a continuation-triggered instruction suffix can substantially increase jailbreak success rates. To uncover the intrinsic mechanisms of this phenomenon, we conduct a comprehensive mechanistic interpretability analysis at the level of attention heads. Through causal interventions and activation scaling, we show that this jailbreak behavior primarily arises from an inherent competition between the model's intrinsic continuation drive and the safety defenses acquired through alignment training. Furthermore, we perform a detailed behavioral analysis of the identified safety-critical attention heads, revealing notable differences in the functions and behaviors of safety heads across different model architectures. These findings provide a novel mechanistic perspective for understanding and interpreting jailbreak behaviors in LLMs, offering both theoretical insights and practical implications for improving model safety.

