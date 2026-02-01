---
layout: default
title: Language-based Trial and Error Falls Behind in the Era of Experience
---

# Language-based Trial and Error Falls Behind in the Era of Experience
**arXiv**：[2601.21754v1](https://arxiv.org/abs/2601.21754) · [PDF](https://arxiv.org/pdf/2601.21754.pdf)  
**作者**：Haoyu Wang, Guozheng Ma, Shugang Cui, Yilun Kong, Haotian Luo, Li Shen, Mengya Gao, Yichao Wu, Xiaogang Wang, Dacheng Tao  

**一句话要点**：提出SCOUT框架以解决大语言模型在非语言环境中探索成本过高的问题

**关键词**：大语言模型, 探索与利用, 强化学习, 非语言任务, 计算效率

## 3 点简述
- 核心问题：大语言模型在非语言任务中因探索成本过高而性能受限
- 方法要点：使用轻量级scouts快速探索环境，再通过微调和强化学习引导大语言模型
- 实验或效果：SCOUT使Qwen2.5-3B-Instruct模型平均得分0.86，优于Gemini-2.5-Pro，节省约60%GPU时间

## 摘要（原文）

> While Large Language Models (LLMs) excel in language-based agentic tasks, their applicability to unseen, nonlinguistic environments (e.g., symbolic or spatial tasks) remains limited. Previous work attributes this performance gap to the mismatch between the pretraining distribution and the testing distribution. In this work, we demonstrate the primary bottleneck is the prohibitive cost of exploration: mastering these tasks requires extensive trial-and-error, which is computationally unsustainable for parameter-heavy LLMs operating in a high dimensional semantic space. To address this, we propose SCOUT (Sub-Scale Collaboration On Unseen Tasks), a novel framework that decouples exploration from exploitation. We employ lightweight "scouts" (e.g., small MLPs) to probe environmental dynamics at a speed and scale far exceeding LLMs. The collected trajectories are utilized to bootstrap the LLM via Supervised Fine-Tuning (SFT), followed by multi-turn Reinforcement Learning (RL) to activate its latent world knowledge. Empirically, SCOUT enables a Qwen2.5-3B-Instruct model to achieve an average score of 0.86, significantly outperforming proprietary models, including Gemini-2.5-Pro (0.60), while saving about 60% GPU hours consumption.

