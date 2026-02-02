---
layout: default
title: Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
---

# Learning with Challenges: Adaptive Difficulty-Aware Data Generation for Mobile GUI Agent Training
**arXiv**：[2601.22781v1](https://arxiv.org/abs/2601.22781) · [PDF](https://arxiv.org/pdf/2601.22781.pdf)  
**作者**：Linjia Kang, Zhimin Wang, Yongkang Zhang, Duo Wu, Jinghe Wang, Ming Ma, Haopeng Yan, Zhi Wang  

**一句话要点**：提出MobileGen框架，通过自适应难度数据生成提升移动GUI代理训练效果

**关键词**：移动GUI代理, 自适应难度生成, 数据生成框架, 交互轨迹合成, 能力边界评估

## 3 点简述
- 核心问题：现有移动GUI代理训练数据生成方法缺乏对任务难度的细粒度控制，导致训练难度与代理能力不匹配
- 方法要点：MobileGen将任务难度解耦为结构和语义维度，基于代理能力边界自适应采样难度并生成高质量交互轨迹
- 实验或效果：在多个基准测试中，MobileGen使GUI代理平均性能提升1.57倍，优于现有数据生成方法

## 摘要（原文）

> Large-scale, high-quality interaction trajectories are essential for advancing mobile Graphical User Interface (GUI) agents. While existing methods typically rely on labor-intensive human demonstrations or automated model exploration to generate GUI trajectories, they lack fine-grained control over task difficulty. This fundamentally restricts learning effectiveness due to the mismatch between the training difficulty and the agent's capabilities. Inspired by how humans acquire skills through progressively challenging tasks, we propose MobileGen, a novel data generation framework that adaptively aligns training difficulty with the GUI agent's capability frontier. Specifically, MobileGen explicitly decouples task difficulty into structural (e.g., trajectory length) and semantic (e.g., task goal) dimensions. It then iteratively evaluates the agent on a curated prior dataset to construct a systematic profile of its capability frontier across these two dimensions. With this profile, the probability distribution of task difficulty is adaptively computed, from which the target difficulty for the next round of training can be sampled. Guided by the sampled difficulty, a multi-agent controllable generator is finally used to synthesize high-quality interaction trajectories along with corresponding task instructions. Extensive experiments show that MobileGen consistently outperforms existing data generation methods by improving the average performance of GUI agents by 1.57 times across multiple challenging benchmarks. This highlights the importance of capability-aligned data generation for effective mobile GUI agent training.

