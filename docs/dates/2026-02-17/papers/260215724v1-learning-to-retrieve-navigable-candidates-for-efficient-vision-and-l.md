---
layout: default
title: Learning to Retrieve Navigable Candidates for Efficient Vision-and-Language Navigation
---

# Learning to Retrieve Navigable Candidates for Efficient Vision-and-Language Navigation
**arXiv**：[2602.15724v1](https://arxiv.org/abs/2602.15724) · [PDF](https://arxiv.org/pdf/2602.15724.pdf)  
**作者**：Shutian Gu, Chengkai Huang, Ruoyu Wang, Lina Yao  

**一句话要点**：提出检索增强框架以提升基于大语言模型的视觉语言导航效率与稳定性

**关键词**：视觉语言导航, 检索增强, 大语言模型, 轨迹检索, 候选剪枝, 模块化框架

## 3 点简述
- 核心问题：基于提示的大语言模型导航决策效率低，需重复解释指令并处理噪声候选方向
- 方法要点：引入两级检索，包括指令级嵌入检索轨迹示例和模仿学习候选检索器剪枝方向
- 实验或效果：在R2R基准上，成功率和SPL等指标在可见与未见环境中均获提升

## 摘要（原文）

> Vision-and-Language Navigation (VLN) requires an agent to follow natural-language instructions and navigate through previously unseen environments. Recent approaches increasingly employ large language models (LLMs) as high-level navigators due to their flexibility and reasoning capability. However, prompt-based LLM navigation often suffers from inefficient decision-making, as the model must repeatedly interpret instructions from scratch and reason over noisy and verbose navigable candidates at each step. In this paper, we propose a retrieval-augmented framework to improve the efficiency and stability of LLM-based VLN without modifying or fine-tuning the underlying language model. Our approach introduces retrieval at two complementary levels. At the episode level, an instruction-level embedding retriever selects semantically similar successful navigation trajectories as in-context exemplars, providing task-specific priors for instruction grounding. At the step level, an imitation-learned candidate retriever prunes irrelevant navigable directions before LLM inference, reducing action ambiguity and prompt complexity. Both retrieval modules are lightweight, modular, and trained independently of the LLM. We evaluate our method on the Room-to-Room (R2R) benchmark. Experimental results demonstrate consistent improvements in Success Rate, Oracle Success Rate, and SPL on both seen and unseen environments. Ablation studies further show that instruction-level exemplar retrieval and candidate pruning contribute complementary benefits to global guidance and step-wise decision efficiency. These results indicate that retrieval-augmented decision support is an effective and scalable strategy for enhancing LLM-based vision-and-language navigation.

