---
layout: default
title: MobileDreamer: Generative Sketch World Model for GUI Agent
---

# MobileDreamer: Generative Sketch World Model for GUI Agent
**arXiv**：[2601.04035v1](https://arxiv.org/abs/2601.04035) · [PDF](https://arxiv.org/pdf/2601.04035.pdf)  
**作者**：Yilin Cao, Yufeng Zhong, Zhixiong Zeng, Liming Zheng, Jing Huang, Haibo Qiu, Peng Shi, Wenji Mao, Wan Guanglu  

**一句话要点**：提出MobileDreamer世界模型框架，以提升移动GUI代理在长时任务中的决策性能。

**关键词**：移动GUI代理, 世界模型, 文本草图建模, 顺序不变学习, 长时任务决策, Android World

## 3 点简述
- 核心问题：现有移动GUI代理多为反应式，依赖当前屏幕，长时任务性能受限。
- 方法要点：基于文本草图世界模型预测动作后状态，采用顺序不变学习策略保持空间信息。
- 实验或效果：在Android World上实现SOTA，任务成功率提升5.25%，模型验证准确预测关键GUI元素。

## 摘要（原文）

> Mobile GUI agents have shown strong potential in real-world automation and practical applications. However, most existing agents remain reactive, making decisions mainly from current screen, which limits their performance on long-horizon tasks. Building a world model from repeated interactions enables forecasting action outcomes and supports better decision making for mobile GUI agents. This is challenging because the model must predict post-action states with spatial awareness while remaining efficient enough for practical deployment. In this paper, we propose MobileDreamer, an efficient world-model-based lookahead framework to equip the GUI agents based on the future imagination provided by the world model. It consists of textual sketch world model and rollout imagination for GUI agent. Textual sketch world model forecasts post-action states through a learning process to transform digital images into key task-related sketches, and designs a novel order-invariant learning strategy to preserve the spatial information of GUI elements. The rollout imagination strategy for GUI agent optimizes the action-selection process by leveraging the prediction capability of world model. Experiments on Android World show that MobileDreamer achieves state-of-the-art performance and improves task success by 5.25%. World model evaluations further verify that our textual sketch modeling accurately forecasts key GUI elements.

