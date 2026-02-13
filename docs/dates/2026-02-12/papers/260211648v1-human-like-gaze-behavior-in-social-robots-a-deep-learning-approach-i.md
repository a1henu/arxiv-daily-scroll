---
layout: default
title: Human-Like Gaze Behavior in Social Robots: A Deep Learning Approach Integrating Human and Non-Human Stimuli
---

# Human-Like Gaze Behavior in Social Robots: A Deep Learning Approach Integrating Human and Non-Human Stimuli
**arXiv**：[2602.11648v1](https://arxiv.org/abs/2602.11648) · [PDF](https://arxiv.org/pdf/2602.11648.pdf)  
**作者**：Faezeh Vahedi, Morteza Memari, Ramtin Tabatabaei, Alireza Taheri  

**一句话要点**：提出集成人类与非人类刺激的深度学习模型，以提升社交机器人的人性化注视行为

**关键词**：社交机器人, 注视行为预测, 深度学习, 非人类刺激, 虚拟现实数据收集

## 3 点简述
- 核心问题：社交机器人需在包含人类与非人类刺激的复杂情境中模拟人类注视行为，以增强交互效果
- 方法要点：使用LSTM和Transformer神经网络，基于VR收集的注视数据训练预测模型
- 实验或效果：模型在动画和真实场景中预测准确率达67.6%-72%，部署于NAO机器人获高满意度评价

## 摘要（原文）

> Nonverbal behaviors, particularly gaze direction, play a crucial role in enhancing effective communication in social interactions. As social robots increasingly participate in these interactions, they must adapt their gaze based on human activities and remain receptive to all cues, whether human-generated or not, to ensure seamless and effective communication. This study aims to increase the similarity between robot and human gaze behavior across various social situations, including both human and non-human stimuli (e.g., conversations, pointing, door openings, and object drops). A key innovation in this study, is the investigation of gaze responses to non-human stimuli, a critical yet underexplored area in prior research. These scenarios, were simulated in the Unity software as a 3D animation and a 360-degree real-world video. Data on gaze directions from 41 participants were collected via virtual reality (VR) glasses. Preprocessed data, trained two neural networks-LSTM and Transformer-to build predictive models based on individuals' gaze patterns. In the animated scenario, the LSTM and Transformer models achieved prediction accuracies of 67.6% and 70.4%, respectively; In the real-world scenario, the LSTM and Transformer models achieved accuracies of 72% and 71.6%, respectively. Despite the gaze pattern differences among individuals, our models outperform existing approaches in accuracy while uniquely considering non-human stimuli, offering a significant advantage over previous literature. Furthermore, deployed on the NAO robot, the system was evaluated by 275 participants via a comprehensive questionnaire, with results demonstrating high satisfaction during interactions. This work advances social robotics by enabling robots to dynamically mimic human gaze behavior in complex social contexts.

