---
layout: default
title: Talk2DM: Enabling Natural Language Querying and Commonsense Reasoning for Vehicle-Road-Cloud Integrated Dynamic Maps with Large Language Models
---

# Talk2DM: Enabling Natural Language Querying and Commonsense Reasoning for Vehicle-Road-Cloud Integrated Dynamic Maps with Large Language Models
**arXiv**：[2602.11860v1](https://arxiv.org/abs/2602.11860) · [PDF](https://arxiv.org/pdf/2602.11860.pdf)  
**作者**：Lu Tao, Jinxuan Luo, Yousuke Watanabe, Zhengshu Zhou, Yuhuan Lu, Shen Ying, Pan Zhang, Fei Zhao, Hiroaki Takada  

**一句话要点**：提出Talk2DM模块，通过链式提示机制为车路云动态地图系统添加自然语言查询与常识推理能力。

**关键词**：动态地图, 自然语言查询, 常识推理, 车路云协同, 链式提示, 仿真框架

## 3 点简述
- 核心问题：现有动态地图系统缺乏自然语言接口，限制了人机交互效率。
- 方法要点：基于VRCsim仿真框架构建VRC-QA数据集，并设计链式提示机制整合规则与LLM常识。
- 实验或效果：在VRC-QA上，Talk2DM支持多LLM切换，NLS查询准确率超93%，响应时间2-5秒。

## 摘要（原文）

> Dynamic maps (DM) serve as the fundamental information infrastructure for vehicle-road-cloud (VRC) cooperative autonomous driving in China and Japan. By providing comprehensive traffic scene representations, DM overcome the limitations of standalone autonomous driving systems (ADS), such as physical occlusions. Although DM-enhanced ADS have been successfully deployed in real-world applications in Japan, existing DM systems still lack a natural-language-supported (NLS) human interface, which could substantially enhance human-DM interaction. To address this gap, this paper introduces VRCsim, a VRC cooperative perception (CP) simulation framework designed to generate streaming VRC-CP data. Based on VRCsim, we construct a question-answering data set, VRC-QA, focused on spatial querying and reasoning in mixed-traffic scenes. Building upon VRCsim and VRC-QA, we further propose Talk2DM, a plug-and-play module that extends VRC-DM systems with NLS querying and commonsense reasoning capabilities. Talk2DM is built upon a novel chain-of-prompt (CoP) mechanism that progressively integrates human-defined rules with the commonsense knowledge of large language models (LLMs). Experiments on VRC-QA show that Talk2DM can seamlessly switch across different LLMs while maintaining high NLS query accuracy, demonstrating strong generalization capability. Although larger models tend to achieve higher accuracy, they incur significant efficiency degradation. Our results reveal that Talk2DM, powered by Qwen3:8B, Gemma3:27B, and GPT-oss models, achieves over 93\% NLS query accuracy with an average response time of only 2-5 seconds, indicating strong practical potential.

