---
layout: default
title: Feature-Selective Representation Misdirection for Machine Unlearning
---

# Feature-Selective Representation Misdirection for Machine Unlearning
**arXiv**：[2512.16297v1](https://arxiv.org/abs/2512.16297) · [PDF](https://arxiv.org/pdf/2512.16297.pdf)  
**作者**：Taozhao Chen, Linghan Huang, Kim-Kwang Raymond Choo, Huaming Chen  

**一句话要点**：提出选择性表示误导框架以解决大语言模型在分布纠缠场景下的安全遗忘问题

**关键词**：机器遗忘, 大语言模型, 安全合规, 激活编辑, 特征选择, 表示误导

## 3 点简述
- 核心问题：现有遗忘方法假设遗忘与保留数据集清晰分离，难以处理分布高度纠缠的操作场景
- 方法要点：基于激活编辑，使用特征感知和方向可控的扰动，选择性抑制有害表示
- 实验或效果：在WMDP基准测试中实现先进遗忘性能，最小化效用损失，并在20-30%重叠下保持有效

## 摘要（原文）

> As large language models (LLMs) are increasingly adopted in safety-critical and regulated sectors, the retention of sensitive or prohibited knowledge introduces escalating risks, ranging from privacy leakage to regulatory non-compliance to to potential misuse, and so on. Recent studies suggest that machine unlearning can help ensure deployed models comply with evolving legal, safety, and governance requirements. However, current unlearning techniques assume clean separation between forget and retain datasets, which is challenging in operational settings characterized by highly entangled distributions. In such scenarios, perturbation-based methods often degrade general model utility or fail to ensure safety. To address this, we propose Selective Representation Misdirection for Unlearning (SRMU), a novel principled activation-editing framework that enforces feature-aware and directionally controlled perturbations. Unlike indiscriminate model weights perturbations, SRMU employs a structured misdirection vector with an activation importance map. The goal is to allow SRMU selectively suppresses harmful representations while preserving the utility on benign ones. Experiments are conducted on the widely used WMDP benchmark across low- and high-entanglement configurations. Empirical results reveal that SRMU delivers state-of-the-art unlearning performance with minimal utility losses, and remains effective under 20-30\% overlap where existing baselines collapse. SRMU provides a robust foundation for safety-driven model governance, privacy compliance, and controlled knowledge removal in the emerging LLM-based applications. We release the replication package at https://figshare.com/s/d5931192a8824de26aff.

