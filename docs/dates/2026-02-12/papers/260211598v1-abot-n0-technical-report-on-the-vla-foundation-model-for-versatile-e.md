---
layout: default
title: ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation
---

# ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation
**arXiv**：[2602.11598v1](https://arxiv.org/abs/2602.11598) · [PDF](https://arxiv.org/pdf/2602.11598.pdf)  
**作者**：Zedong Chu, Shichao Xie, Xiaolong Wu, Yanfen Shen, Minghua Luo, Zhengbo Wang, Fei Liu, Xiaoxu Leng, Junjun Hu, Mingyang Yin, Jia Lu, Yingnan Guo, Kai Yang, Jiawei Han, Xu Chen, Yanqing Zhu, Yuxiang Zhao, Xin Liu, Yirong Yang, Ye He, Jiahang Wang, Yang Cai, Tianlin Zhang, Li Gao, Liu Liu, Mingchao Sun, Fan Jiang, Chiyu Wang, Zhicheng Liu, Hongyu Pan, Honglin Han, Zhining Gu, Kuan Yang, Jianfang Zhang, Di Jing, Zihao Guan, Wei Guo, Guoqing Liu, Di Yang, Xiangpo Yang, Menglin Yang, Hongguang Xing, Weiguo Li, Mu Xu  

**一句话要点**：提出ABot-N0统一VLA基础模型，实现5个核心具身导航任务的整合与SOTA性能。

**关键词**：具身导航, 视觉-语言-动作模型, 基础模型, 流匹配, 分层架构, 拓扑记忆

## 3 点简述
- 核心问题：具身导航长期依赖任务特定架构，导致碎片化。
- 方法要点：采用分层‘大脑-动作’架构，结合LLM认知大脑与流匹配动作专家。
- 实验或效果：在7个基准测试中实现新SOTA，支持大规模数据学习与动态环境长程任务。

## 摘要（原文）

> Embodied navigation has long been fragmented by task-specific architectures. We introduce ABot-N0, a unified Vision-Language-Action (VLA) foundation model that achieves a ``Grand Unification'' across 5 core tasks: Point-Goal, Object-Goal, Instruction-Following, POI-Goal, and Person-Following. ABot-N0 utilizes a hierarchical ``Brain-Action'' architecture, pairing an LLM-based Cognitive Brain for semantic reasoning with a Flow Matching-based Action Expert for precise, continuous trajectory generation.
>   To support large-scale learning, we developed the ABot-N0 Data Engine, curating 16.9M expert trajectories and 5.0M reasoning samples across 7,802 high-fidelity 3D scenes (10.7 $\text{km}^2$). ABot-N0 achieves new SOTA performance across 7 benchmarks, significantly outperforming specialized models. Furthermore, our Agentic Navigation System integrates a planner with hierarchical topological memory, enabling robust, long-horizon missions in dynamic real-world environments.

