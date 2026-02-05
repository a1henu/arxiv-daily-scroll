---
layout: default
title: AppleVLM: End-to-end Autonomous Driving with Advanced Perception and Planning-Enhanced Vision-Language Models
---

# AppleVLM: End-to-end Autonomous Driving with Advanced Perception and Planning-Enhanced Vision-Language Models
**arXiv**：[2602.04256v1](https://arxiv.org/abs/2602.04256) · [PDF](https://arxiv.org/pdf/2602.04256.pdf)  
**作者**：Yuxuan Han, Kunyuan Wu, Qianyi Shao, Renxiang Xiao, Zilu Wang, Cansen Jiang, Yi Xiao, Liang Hu, Yunjiang Lou  

**一句话要点**：提出AppleVLM以增强端到端自动驾驶的感知与规划能力

**关键词**：端到端自动驾驶, 视觉语言模型, 时空融合, 鸟瞰图规划, 分层思维链, 真实世界部署

## 3 点简述
- 核心问题：现有VLM方法存在车道感知不足、语言理解偏差和角点处理困难。
- 方法要点：引入时空融合视觉编码器和鸟瞰图规划模态，结合分层思维链微调解码器。
- 实验或效果：在CARLA基准测试中实现最优性能，并在真实AGV平台上成功演示。

## 摘要（原文）

> End-to-end autonomous driving has emerged as a promising paradigm integrating perception, decision-making, and control within a unified learning framework. Recently, Vision-Language Models (VLMs) have gained significant attention for their potential to enhance the robustness and generalization of end-to-end driving models in diverse and unseen scenarios. However, existing VLM-based approaches still face challenges, including suboptimal lane perception, language understanding biases, and difficulties in handling corner cases. To address these issues, we propose AppleVLM, an advanced perception and planning-enhanced VLM model for robust end-to-end driving. AppleVLM introduces a novel vision encoder and a planning strategy encoder to improve perception and decision-making. Firstly, the vision encoder fuses spatial-temporal information from multi-view images across multiple timesteps using a deformable transformer mechanism, enhancing robustness to camera variations and facilitating scalable deployment across different vehicle platforms. Secondly, unlike traditional VLM-based approaches, AppleVLM introduces a dedicated planning modality that encodes explicit Bird's-Eye-View spatial information, mitigating language biases in navigation instructions. Finally, a VLM decoder fine-tuned by a hierarchical Chain-of-Thought integrates vision, language, and planning features to output robust driving waypoints. We evaluate AppleVLM in closed-loop experiments on two CARLA benchmarks, achieving state-of-the-art driving performance. Furthermore, we deploy AppleVLM on an AGV platform and successfully showcase real-world end-to-end autonomous driving in complex outdoor environments.

