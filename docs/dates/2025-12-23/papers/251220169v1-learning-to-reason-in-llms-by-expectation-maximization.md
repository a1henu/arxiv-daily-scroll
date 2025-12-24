---
layout: default
title: Learning to Reason in LLMs by Expectation Maximization
---

# Learning to Reason in LLMs by Expectation Maximization
**arXiv**：[2512.20169v1](https://arxiv.org/abs/2512.20169) · [PDF](https://arxiv.org/pdf/2512.20169.pdf)  
**作者**：Junghyun Lee, Branislav Kveton, Sunav Choudhary, Subhojyoti Mukherjee, Anup Rao, Ryan A. Rossi, Alexa Siu  

**一句话要点**：提出基于期望最大化的推理学习方法，通过采样方案优化大语言模型推理性能

**关键词**：大语言模型推理, 期望最大化, 采样方案优化, 隐变量模型, 推理学习

## 3 点简述
- 将LLM推理形式化为隐变量模型，推导出期望最大化目标以学习推理过程
- 比较多种采样方案，包括拒绝采样、STaR和仅保留推理阶段的PPS
- 在ARC、MMLU和OpenBookQA数据集上实验，PPS方案在Llama和Qwen模型中表现最佳

## 摘要（原文）

> Large language models (LLMs) solve reasoning problems by first generating a rationale and then answering. We formalize reasoning as a latent variable model and derive an expectation-maximization (EM) objective for learning to reason. This view connects EM and modern reward-based optimization, and shows that the main challenge lies in designing a sampling distribution that generates rationales that justify correct answers. We instantiate and compare several sampling schemes: rejection sampling with a budget, self-taught reasoner (STaR), and prompt posterior sampling (PPS), which only keeps the rationalization stage of STaR. Our experiments on the ARC, MMLU, and OpenBookQA datasets with the Llama and Qwen models show that the sampling scheme can significantly affect the accuracy of learned reasoning models. Despite its simplicity, we observe that PPS outperforms the other sampling schemes.

