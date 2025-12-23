---
layout: default
title: FC-MIR: A Mobile Screen Awareness Framework for Intent-Aware Recommendation based on Frame-Compressed Multimodal Trajectory Reasoning
---

# FC-MIR: A Mobile Screen Awareness Framework for Intent-Aware Recommendation based on Frame-Compressed Multimodal Trajectory Reasoning
**arXiv**：[2512.19107v1](https://arxiv.org/abs/2512.19107) · [PDF](https://arxiv.org/pdf/2512.19107.pdf)  
**作者**：Zhe Yang, Xiaoshuang Sheng, Zhengnan Zhang, Jidong Wu, Zexing Wang, Xin He, Shenghua Xu, Guanjing Xiong  

**一句话要点**：提出FC-MIR框架，通过帧压缩多模态轨迹推理实现移动屏幕意图感知推荐，以提升效率。

**关键词**：移动屏幕感知, 多模态轨迹推理, 帧压缩, 意图预测, UI轨迹数据集, 轻量部署

## 3 点简述
- 核心问题：MLLMs在移动设备实时部署中面临计算成本高和冗余帧处理效率低的问题。
- 方法要点：采用关键帧采样和自适应拼接减少视觉冗余，集成MLLMs进行轨迹总结和意图预测。
- 实验或效果：压缩率50%-60%时性能保持，MLLMs在意图总结方面表现强，但建议生成有待改进。

## 摘要（原文）

> Identifying user intent from mobile UI operation trajectories is critical for advancing UI understanding and enabling task automation agents. While Multimodal Large Language Models (MLLMs) excel at video understanding tasks, their real-time mobile deployment is constrained by heavy computational costs and inefficient redundant frame processing. To address these issues, we propose the FC-MIR framework: leveraging keyframe sampling and adaptive concatenation, it cuts visual redundancy to boost inference efficiency, while integrating state-of-the-art closed-source MLLMs or fine-tuned models (e.g., Qwen3-VL) for trajectory summarization and intent prediction. We further expand task scope to explore generating post-prediction operations and search suggestions, and introduce a fine-grained metric to evaluate the practical utility of summaries, predictions, and suggestions. For rigorous assessment, we construct a UI trajectory dataset covering scenarios from UI-Agents (Agent-I) and real user interactions (Person-I). Experimental results show our compression method retains performance at 50%-60% compression rates; both closed-source and fine-tuned MLLMs demonstrate strong intent summarization, supporting potential lightweight on-device deployment. However, MLLMs still struggle with useful and "surprising" suggestions, leaving room for improvement. Finally, we deploy the framework in a real-world setting, integrating UI perception and UI-Agent proxies to lay a foundation for future progress in this field.

