---
layout: default
title: Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance
---

# Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance
**arXiv**：[2601.01887v1](https://arxiv.org/abs/2601.01887) · [PDF](https://arxiv.org/pdf/2601.01887.pdf)  
**作者**：Jiawen Zhang, Lipeng He, Kejia Chen, Jian Lou, Jian Liu, Xiaohu Yang, Ruoxi Jia  

**一句话要点**：提出单实例安全补丁方法，以恢复微调后大语言模型的安全性，无需牺牲实用性。

**关键词**：大语言模型安全对齐, 单实例微调, 安全梯度低秩结构, 模型实用性保持, 高效安全恢复

## 3 点简述
- 微调安全对齐大语言模型会显著降低其安全性，传统方法需大量安全样本或校准集，计算开销大且损害模型实用性。
- 研究发现仅需单个安全示例即可完全恢复安全性，不影响实用性，成本低，且适用于不同模型和有害示例数量。
- 揭示安全梯度的低秩结构，解释高效修正的可行性，并在多个模型和数据集上验证方法的通用性。

## 摘要（原文）

> Fine-tuning safety-aligned large language models (LLMs) can substantially compromise their safety. Previous approaches require many safety samples or calibration sets, which not only incur significant computational overhead during realignment but also lead to noticeable degradation in model utility. Contrary to this belief, we show that safety alignment can be fully recovered with only a single safety example, without sacrificing utility and at minimal cost. Remarkably, this recovery is effective regardless of the number of harmful examples used in fine-tuning or the size of the underlying model, and convergence is achieved within just a few epochs. Furthermore, we uncover the low-rank structure of the safety gradient, which explains why such efficient correction is possible. We validate our findings across five safety-aligned LLMs and multiple datasets, demonstrating the generality of our approach.

