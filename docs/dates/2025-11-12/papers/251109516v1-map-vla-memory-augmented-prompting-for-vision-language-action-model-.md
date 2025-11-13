---
layout: default
title: MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
---

# MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation
**arXiv**：[2511.09516v1](https://arxiv.org/abs/2511.09516) · [PDF](https://arxiv.org/pdf/2511.09516.pdf)  
**作者**：Runhao Li, Wenkai Guo, Zhenyu Wu, Changyuan Wang, Haoyuan Deng, Zhenyu Weng, Yap-Peng Tan, Ziwei Wang  

**一句话要点**：提出MAP-VLA框架，通过记忆增强提示解决机器人长时程操作任务中的记忆缺失问题。

**关键词**：机器人操作, 视觉语言动作模型, 记忆增强, 提示调优, 长时程任务, 检索增强

## 3 点简述
- 核心问题：预训练VLA模型在长时程任务中因缺乏记忆而表现不佳。
- 方法要点：构建演示记忆库，通过相似性检索动态集成软提示增强动作生成。
- 实验或效果：在仿真和真实机器人评估中性能提升达7.0%和25.0%。

## 摘要（原文）

> Pre-trained Vision-Language-Action (VLA) models have achieved remarkable success in improving robustness and generalization for end-to-end robotic manipulation. However, these models struggle with long-horizon tasks due to their lack of memory and reliance solely on immediate sensory inputs. To address this limitation, we propose Memory-Augmented Prompting for Vision-Language-Action model (MAP-VLA), a novel framework that empowers pre-trained VLA models with demonstration-derived memory prompts to augment action generation for long-horizon robotic manipulation tasks. To achieve this, MAP-VLA first constructs a memory library from historical demonstrations, where each memory unit captures information about a specific stage of a task. These memory units are implemented as learnable soft prompts optimized through prompt tuning. Then, during real-time task execution, MAP-VLA retrieves relevant memory through trajectory similarity matching and dynamically integrates it into the VLA model for augmented action generation. Importantly, this prompt tuning and retrieval augmentation approach operates as a plug-and-play module for a frozen VLA model, offering a lightweight and flexible solution to improve task performance. Experimental results show that MAP-VLA delivers up to 7.0% absolute performance gains in the simulation benchmark and 25.0% on real robot evaluations for long-horizon tasks, surpassing the current state-of-the-art methods.

