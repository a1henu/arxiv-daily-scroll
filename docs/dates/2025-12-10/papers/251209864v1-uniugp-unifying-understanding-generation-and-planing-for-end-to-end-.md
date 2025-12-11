---
layout: default
title: UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving
---

# UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving
**arXiv**：[2512.09864v1](https://arxiv.org/abs/2512.09864) · [PDF](https://arxiv.org/pdf/2512.09864.pdf)  
**作者**：Hao Lu, Ziyang Liu, Guangfeng Jiang, Yuanfei Luo, Sheng Chen, Yangang Zhang, Ying-Cong Chen  

**一句话要点**：提出UniUGP框架以统一理解、生成和规划，提升自动驾驶在长尾场景中的性能。

**关键词**：自动驾驶, 视觉语言动作模型, 视频生成, 轨迹规划, 长尾场景, 混合专家架构

## 3 点简述
- 核心问题：自动驾驶系统在长尾场景中因世界知识有限和视觉动态建模弱而表现不佳。
- 方法要点：构建专用数据集，通过混合专家架构整合视觉语言模型和视频生成模型，实现场景推理、未来视频生成和轨迹规划的统一。
- 实验或效果：在感知、推理和决策方面达到先进水平，对挑战性长尾场景具有优越泛化能力。

## 摘要（原文）

> Autonomous driving (AD) systems struggle in long-tail scenarios due to limited world knowledge and weak visual dynamic modeling. Existing vision-language-action (VLA)-based methods cannot leverage unlabeled videos for visual causal learning, while world model-based methods lack reasoning capabilities from large language models. In this paper, we construct multiple specialized datasets providing reasoning and planning annotations for complex scenarios. Then, a unified Understanding-Generation-Planning framework, named UniUGP, is proposed to synergize scene reasoning, future video generation, and trajectory planning through a hybrid expert architecture. By integrating pre-trained VLMs and video generation models, UniUGP leverages visual dynamics and semantic reasoning to enhance planning performance. Taking multi-frame observations and language instructions as input, it produces interpretable chain-of-thought reasoning, physically consistent trajectories, and coherent future videos. We introduce a four-stage training strategy that progressively builds these capabilities across multiple existing AD datasets, along with the proposed specialized datasets. Experiments demonstrate state-of-the-art performance in perception, reasoning, and decision-making, with superior generalization to challenging long-tail situations.

