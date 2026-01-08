---
layout: default
title: O-Researcher: An Open Ended Deep Research Model via Multi-Agent Distillation and Agentic RL
---

# O-Researcher: An Open Ended Deep Research Model via Multi-Agent Distillation and Agentic RL
**arXiv**：[2601.03743v1](https://arxiv.org/abs/2601.03743) · [PDF](https://arxiv.org/pdf/2601.03743.pdf)  
**作者**：Yi Yao, He Zhu, Piaohong Wang, Jincheng Ren, Xinlong Yang, Qianben Chen, Xiaowan Li, Dingfeng Shi, Jiaxian Li, Qiexiang Wang, Sinuo Wang, Xinpeng Liu, Jiaqi Wu, Minghao Liu, Wangchunshu Zhou  

**一句话要点**：提出多智能体蒸馏与强化学习框架，以自动合成高质量研究数据，提升开源大语言模型性能。

**关键词**：大语言模型, 数据合成, 多智能体系统, 强化学习, 开源模型优化, 研究基准测试

## 3 点简述
- 核心问题：开源与闭源大语言模型性能差距源于高质量训练数据获取不均。
- 方法要点：采用多智能体协作模拟工具集成推理，自动生成研究级指令数据，结合监督微调与强化学习进行训练。
- 实验或效果：在深度研究基准测试中，使开源模型达到新最优性能，验证框架有效性。

## 摘要（原文）

> The performance gap between closed-source and open-source large language models (LLMs) is largely attributed to disparities in access to high-quality training data. To bridge this gap, we introduce a novel framework for the automated synthesis of sophisticated, research-grade instructional data. Our approach centers on a multi-agent workflow where collaborative AI agents simulate complex tool-integrated reasoning to generate diverse and high-fidelity data end-to-end. Leveraging this synthesized data, we develop a two-stage training strategy that integrates supervised fine-tuning with a novel reinforcement learning method, designed to maximize model alignment and capability. Extensive experiments demonstrate that our framework empowers open-source models across multiple scales, enabling them to achieve new state-of-the-art performance on the major deep research benchmark. This work provides a scalable and effective pathway for advancing open-source LLMs without relying on proprietary data or models.

