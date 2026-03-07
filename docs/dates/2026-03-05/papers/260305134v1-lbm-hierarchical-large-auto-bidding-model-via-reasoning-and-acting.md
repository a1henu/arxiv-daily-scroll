---
layout: default
title: LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting
---

# LBM: Hierarchical Large Auto-Bidding Model via Reasoning and Acting
**arXiv**：[2603.05134v1](https://arxiv.org/abs/2603.05134) · [PDF](https://arxiv.org/pdf/2603.05134.pdf)  
**作者**：Yewen Li, Zhiyi Lyu, Peng Jiang, Qingpeng Cai, Fei Pan, Bo An, Peng Jiang  

**一句话要点**：提出分层大自动竞价模型LBM，利用大语言模型推理能力优化在线广告竞价策略。

**关键词**：自动竞价, 大语言模型, 分层模型, 离线强化学习, 多模态融合

## 3 点简述
- 核心问题：现有自动竞价方法因黑盒训练和数据覆盖有限，在动态广告环境中泛化能力差。
- 方法要点：设计LBM-Think进行推理和LBM-Act生成动作，通过双嵌入机制融合语言与数值输入，并采用GQPO离线强化微调减少幻觉。
- 实验或效果：实验显示基于LBM的生成模型在训练效率和泛化能力上表现优越。

## 摘要（原文）

> The growing scale of ad auctions on online advertising platforms has intensified competition, making manual bidding impractical and necessitating auto-bidding to help advertisers achieve their economic goals. Current auto-bidding methods have evolved to use offline reinforcement learning or generative methods to optimize bidding strategies, but they can sometimes behave counterintuitively due to the black-box training manner and limited mode coverage of datasets, leading to challenges in understanding task status and generalization in dynamic ad environments. Large language models (LLMs) offer a promising solution by leveraging prior human knowledge and reasoning abilities to improve auto-bidding performance. However, directly applying LLMs to auto-bidding faces difficulties due to the need for precise actions in competitive auctions and the lack of specialized auto-bidding knowledge, which can lead to hallucinations and suboptimal decisions. To address these challenges, we propose a hierarchical Large autoBidding Model (LBM) to leverage the reasoning capabilities of LLMs for developing a superior auto-bidding strategy. This includes a high-level LBM-Think model for reasoning and a low-level LBM-Act model for action generation. Specifically, we propose a dual embedding mechanism to efficiently fuse two modalities, including language and numerical inputs, for language-guided training of the LBM-Act; then, we propose an offline reinforcement fine-tuning technique termed GQPO for mitigating the LLM-Think's hallucinations and enhancing decision-making performance without simulation or real-world rollout like previous multi-turn LLM-based methods. Experiments demonstrate the superiority of a generative backbone based on our LBM, especially in an efficient training manner and generalization ability.

