---
layout: default
title: SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment
---

# SafeThinker: Reasoning about Risk to Deepen Safety Beyond Shallow Alignment
**arXiv**：[2601.16506v1](https://arxiv.org/abs/2601.16506) · [PDF](https://arxiv.org/pdf/2601.16506.pdf)  
**作者**：Xianya Fang, Xianying Luo, Yadong Wang, Xiang Chen, Yu Tian, Zequn Sun, Rui Liu, Jun Fang, Naiqiang Tan, Yuanning Cui, Sheng-Jun Huang  

**一句话要点**：提出SafeThinker框架，通过动态防御资源分配解决大语言模型浅层安全对齐问题。

**关键词**：大语言模型安全, 动态防御框架, 网关分类器, 安全对齐, 越狱攻击防御, 鲁棒性优化

## 3 点简述
- 核心问题：大语言模型现有防御导致浅层安全对齐，易受伪装攻击且降低实用性。
- 方法要点：基于轻量级网关分类器动态路由输入，结合标准化拒绝、安全感知双专家和分布引导思考机制。
- 实验或效果：显著降低多种越狱攻击成功率，不损害实用性，平衡鲁棒性与实用性。

## 摘要（原文）

> Despite the intrinsic risk-awareness of Large Language Models (LLMs), current defenses often result in shallow safety alignment, rendering models vulnerable to disguised attacks (e.g., prefilling) while degrading utility. To bridge this gap, we propose SafeThinker, an adaptive framework that dynamically allocates defensive resources via a lightweight gateway classifier. Based on the gateway's risk assessment, inputs are routed through three distinct mechanisms: (i) a Standardized Refusal Mechanism for explicit threats to maximize efficiency; (ii) a Safety-Aware Twin Expert (SATE) module to intercept deceptive attacks masquerading as benign queries; and (iii) a Distribution-Guided Think (DDGT) component that adaptively intervenes during uncertain generation. Experiments show that SafeThinker significantly lowers attack success rates across diverse jailbreak strategies without compromising utility, demonstrating that coordinating intrinsic judgment throughout the generation process effectively balances robustness and practicality.

