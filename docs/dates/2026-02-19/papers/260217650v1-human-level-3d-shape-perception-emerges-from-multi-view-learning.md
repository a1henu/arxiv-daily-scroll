---
layout: default
title: Human-level 3D shape perception emerges from multi-view learning
---

# Human-level 3D shape perception emerges from multi-view learning
**arXiv**：[2602.17650v1](https://arxiv.org/abs/2602.17650) · [PDF](https://arxiv.org/pdf/2602.17650.pdf)  
**作者**：Tyler Bonnen, Jitendra Malik, Angjoo Kanazawa  

**一句话要点**：提出多视图学习框架以匹配人类3D形状感知水平

**关键词**：三维形状感知, 多视图学习, 视觉-空间目标, 零样本评估, 人类行为预测

## 3 点简述
- 核心问题：如何建模人类从二维视觉输入推断三维结构的能力，现有方法未达人类水平。
- 方法要点：使用视觉-空间目标训练神经网络，从自然场景多视图图像预测相机位置和深度，无需对象先验。
- 实验或效果：零样本评估匹配人类准确度，模型响应预测人类行为细节如错误模式和反应时间。

## 摘要（原文）

> Humans can infer the three-dimensional structure of objects from two-dimensional visual inputs. Modeling this ability has been a longstanding goal for the science and engineering of visual intelligence, yet decades of computational methods have fallen short of human performance. Here we develop a modeling framework that predicts human 3D shape inferences for arbitrary objects, directly from experimental stimuli. We achieve this with a novel class of neural networks trained using a visual-spatial objective over naturalistic sensory data; given a set of images taken from different locations within a natural scene, these models learn to predict spatial information related to these images, such as camera location and visual depth, without relying on any object-related inductive biases. Notably, these visual-spatial signals are analogous to sensory cues readily available to humans. We design a zero-shot evaluation approach to determine the performance of these `multi-view' models on a well established 3D perception task, then compare model and human behavior. Our modeling framework is the first to match human accuracy on 3D shape inferences, even without task-specific training or fine-tuning. Remarkably, independent readouts of model responses predict fine-grained measures of human behavior, including error patterns and reaction times, revealing a natural correspondence between model dynamics and human perception. Taken together, our findings indicate that human-level 3D perception can emerge from a simple, scalable learning objective over naturalistic visual-spatial data. All code, human behavioral data, and experimental stimuli needed to reproduce our findings can be found on our project page.

