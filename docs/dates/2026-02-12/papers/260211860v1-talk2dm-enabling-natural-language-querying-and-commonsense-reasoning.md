---
layout: default
title: Talk2DM: Enabling Natural Language Querying and Commonsense Reasoning for Vehicle-Road-Cloud Integrated Dynamic Maps with Large Language Models
---

# Talk2DM: Enabling Natural Language Querying and Commonsense Reasoning for Vehicle-Road-Cloud Integrated Dynamic Maps with Large Language Models
**arXiv**：[2602.11860v1](https://arxiv.org/abs/2602.11860) · [PDF](https://arxiv.org/pdf/2602.11860.pdf)  
**作者**：Lu Tao, Jinxuan Luo, Yousuke Watanabe, Zhengshu Zhou, Yuhuan Lu, Shen Ying, Pan Zhang, Fei Zhao, Hiroaki Takada  

**一句话要点**：提出Talk2DM模块，通过自然语言查询和常识推理增强车路云动态地图系统。

**关键词**：动态地图, 自然语言查询, 常识推理, 车路云协同, 链式提示, 大语言模型

## 3 点简述
- 动态地图系统缺乏自然语言界面，限制人机交互效率。
- 基于VRCsim和VRC-QA，Talk2DM采用链式提示机制集成规则与LLM常识。
- 实验显示Talk2DM在VRC-QA上实现高查询准确率，响应时间短，具实用潜力。

## 摘要（原文）

> Dynamic maps (DM) serve as the fundamental information infrastructure for vehicle-road-cloud (VRC) cooperative autonomous driving in China and Japan. By providing comprehensive traffic scene representations, DM overcome the limitations of standalone autonomous driving systems (ADS), such as physical occlusions. Although DM-enhanced ADS have been successfully deployed in real-world applications in Japan, existing DM systems still lack a natural-language-supported (NLS) human interface, which could substantially enhance human-DM interaction. To address this gap, this paper introduces VRCsim, a VRC cooperative perception (CP) simulation framework designed to generate streaming VRC-CP data. Based on VRCsim, we construct a question-answering data set, VRC-QA, focused on spatial querying and reasoning in mixed-traffic scenes. Building upon VRCsim and VRC-QA, we further propose Talk2DM, a plug-and-play module that extends VRC-DM systems with NLS querying and commonsense reasoning capabilities. Talk2DM is built upon a novel chain-of-prompt (CoP) mechanism that progressively integrates human-defined rules with the commonsense knowledge of large language models (LLMs). Experiments on VRC-QA show that Talk2DM can seamlessly switch across different LLMs while maintaining high NLS query accuracy, demonstrating strong generalization capability. Although larger models tend to achieve higher accuracy, they incur significant efficiency degradation. Our results reveal that Talk2DM, powered by Qwen3:8B, Gemma3:27B, and GPT-oss models, achieves over 93\% NLS query accuracy with an average response time of only 2-5 seconds, indicating strong practical potential.

