---
layout: default
title: MMhops-R1: Multimodal Multi-hop Reasoning
---

# MMhops-R1: Multimodal Multi-hop Reasoning
**arXiv**：[2512.13573v1](https://arxiv.org/abs/2512.13573) · [PDF](https://arxiv.org/pdf/2512.13573.pdf)  
**作者**：Tao Zhang, Ziqi Zhang, Zongyang Ma, Yuxin Chen, Bing Li, Chunfeng Yuan, Guangting Wang, Fengyun Rao, Ying Shan, Weiming Hu  

**一句话要点**：提出MMhops-R1多模态检索增强生成框架以解决多模态多跳推理的复杂挑战

**关键词**：多模态多跳推理, 检索增强生成, 强化学习, 动态规划, 基准数据集, 知识集成

## 3 点简述
- 现有MLLMs多限于单步推理，缺乏评估多跳能力的复杂基准
- 提出MMhops基准和MMhops-R1框架，利用强化学习优化动态推理路径规划
- 实验显示MMhops-R1显著优于基线，并展示对固定跳数任务的强泛化能力

## 摘要（原文）

> The ability to perform multi-modal multi-hop reasoning by iteratively integrating information across various modalities and external knowledge is critical for addressing complex real-world challenges. However, existing Multi-modal Large Language Models (MLLMs) are predominantly limited to single-step reasoning, as existing benchmarks lack the complexity needed to evaluate and drive multi-hop abilities. To bridge this gap, we introduce MMhops, a novel, large-scale benchmark designed to systematically evaluate and foster multi-modal multi-hop reasoning. MMhops dataset comprises two challenging task formats, Bridging and Comparison, which necessitate that models dynamically construct complex reasoning chains by integrating external knowledge. To tackle the challenges posed by MMhops, we propose MMhops-R1, a novel multi-modal Retrieval-Augmented Generation (mRAG) framework for dynamic reasoning. Our framework utilizes reinforcement learning to optimize the model for autonomously planning reasoning paths, formulating targeted queries, and synthesizing multi-level information. Comprehensive experiments demonstrate that MMhops-R1 significantly outperforms strong baselines on MMhops, highlighting that dynamic planning and multi-modal knowledge integration are crucial for complex reasoning. Moreover, MMhops-R1 demonstrates strong generalization to tasks requiring fixed-hop reasoning, underscoring the robustness of our dynamic planning approach. In conclusion, our work contributes a challenging new benchmark and a powerful baseline model, and we will release the associated code, data, and weights to catalyze future research in this critical area.

