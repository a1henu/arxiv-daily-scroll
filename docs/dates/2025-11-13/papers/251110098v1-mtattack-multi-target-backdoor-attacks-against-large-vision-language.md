---
layout: default
title: MTAttack: Multi-Target Backdoor Attacks against Large Vision-Language Models
---

# MTAttack: Multi-Target Backdoor Attacks against Large Vision-Language Models
**arXiv**：[2511.10098v1](https://arxiv.org/abs/2511.10098) · [PDF](https://arxiv.org/pdf/2511.10098.pdf)  
**作者**：Zihan Wang, Guansong Pang, Wenjun Miao, Jin Zheng, Xiao Bai  

**一句话要点**：提出MTAttack框架以解决大型视觉语言模型中的多目标后门攻击问题

**关键词**：大型视觉语言模型, 多目标后门攻击, 触发器优化, 代理空间划分, 安全漏洞

## 3 点简述
- 核心问题：现有后门攻击仅针对单一目标，多目标攻击因特征干扰难以实现准确映射。
- 方法要点：引入代理空间划分和触发器原型锚定约束，联合优化多个触发器确保独立性和可分性。
- 实验效果：在基准测试中成功率显著高于现有方法，并展示跨数据集泛化性和防御鲁棒性。

## 摘要（原文）

> Recent advances in Large Visual Language Models (LVLMs) have demonstrated impressive performance across various vision-language tasks by leveraging large-scale image-text pretraining and instruction tuning. However, the security vulnerabilities of LVLMs have become increasingly concerning, particularly their susceptibility to backdoor attacks. Existing backdoor attacks focus on single-target attacks, i.e., targeting a single malicious output associated with a specific trigger. In this work, we uncover multi-target backdoor attacks, where multiple independent triggers corresponding to different attack targets are added in a single pass of training, posing a greater threat to LVLMs in real-world applications. Executing such attacks in LVLMs is challenging since there can be many incorrect trigger-target mappings due to severe feature interference among different triggers. To address this challenge, we propose MTAttack, the first multi-target backdoor attack framework for enforcing accurate multiple trigger-target mappings in LVLMs. The core of MTAttack is a novel optimization method with two constraints, namely Proxy Space Partitioning constraint and Trigger Prototype Anchoring constraint. It jointly optimizes multiple triggers in the latent space, with each trigger independently mapping clean images to a unique proxy class while at the same time guaranteeing their separability. Experiments on popular benchmarks demonstrate a high success rate of MTAttack for multi-target attacks, substantially outperforming existing attack methods. Furthermore, our attack exhibits strong generalizability across datasets and robustness against backdoor defense strategies. These findings highlight the vulnerability of LVLMs to multi-target backdoor attacks and underscore the urgent need for mitigating such threats. Code is available at https://github.com/mala-lab/MTAttack.

