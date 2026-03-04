---
layout: default
title: BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation
---

# BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation
**arXiv**：[2603.02816v1](https://arxiv.org/abs/2603.02816) · [PDF](https://arxiv.org/pdf/2603.02816.pdf)  
**作者**：Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu  

**一句话要点**：提出BrandFusion多智能体框架，以解决文本到视频生成中无缝品牌集成任务。

**关键词**：文本到视频生成, 品牌集成, 多智能体框架, 语义对齐, 提示优化, 商业应用

## 3 点简述
- 核心问题：文本到视频生成中自动嵌入品牌时，需平衡提示忠实度、品牌可识别性和集成自然性。
- 方法要点：采用离线品牌知识库构建与在线多智能体协同优化，通过迭代提示精炼实现品牌集成。
- 实验或效果：在多个先进模型上测试20个品牌，BrandFusion在语义保持、品牌识别和集成自然性上显著优于基线。

## 摘要（原文）

> The rapid advancement of text-to-video (T2V) models has revolutionized content creation, yet their commercial potential remains largely untapped. We introduce, for the first time, the task of seamless brand integration in T2V: automatically embedding advertiser brands into prompt-generated videos while preserving semantic fidelity to user intent. This task confronts three core challenges: maintaining prompt fidelity, ensuring brand recognizability, and achieving contextually natural integration. To address them, we propose BrandFusion, a novel multi-agent framework comprising two synergistic phases. In the offline phase (advertiser-facing), we construct a Brand Knowledge Base by probing model priors and adapting to novel brands via lightweight fine-tuning. In the online phase (user-facing), five agents jointly refine user prompts through iterative refinement, leveraging the shared knowledge base and real-time contextual tracking to ensure brand visibility and semantic alignment. Experiments on 18 established and 2 custom brands across multiple state-of-the-art T2V models demonstrate that BrandFusion significantly outperforms baselines in semantic preservation, brand recognizability, and integration naturalness. Human evaluations further confirm higher user satisfaction, establishing a practical pathway for sustainable T2V monetization.

