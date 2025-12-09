---
layout: default
title: Improving action classification with brain-inspired deep networks
---

# Improving action classification with brain-inspired deep networks
**arXiv**：[2512.07729v1](https://arxiv.org/abs/2512.07729) · [PDF](https://arxiv.org/pdf/2512.07729.pdf)  
**作者**：Aidas Aglinskas, Stefano Anzellotti  

**一句话要点**：提出脑启发的双流深度网络以提升动作分类性能，模拟人类对躯体和背景的感知分离。

**关键词**：动作识别, 脑启发网络, 领域特异性, 深度神经网络, 躯体感知, 背景感知

## 3 点简述
- 核心问题：深度神经网络在动作识别中可能过度依赖背景信息，忽视躯体信息，与人类感知模式不同。
- 方法要点：设计脑启发的架构，包含独立的躯体流和背景流，模拟大脑的领域特异性处理。
- 实验或效果：该架构在HAA500数据集上提升性能，且准确率模式更接近人类参与者。

## 摘要（原文）

> Action recognition is also key for applications ranging from robotics to healthcare monitoring. Action information can be extracted from the body pose and movements, as well as from the background scene. However, the extent to which deep neural networks (DNNs) make use of information about the body and information about the background remains unclear. Since these two sources of information may be correlated within a training dataset, DNNs might learn to rely predominantly on one of them, without taking full advantage of the other. Unlike DNNs, humans have domain-specific brain regions selective for perceiving bodies, and regions selective for perceiving scenes. The present work tests whether humans are thus more effective at extracting information from both body and background, and whether building brain-inspired deep network architectures with separate domain-specific streams for body and scene perception endows them with more human-like performance. We first demonstrate that DNNs trained using the HAA500 dataset perform almost as accurately on versions of the stimuli that show both body and background and on versions of the stimuli from which the body was removed, but are at chance-level for versions of the stimuli from which the background was removed. Conversely, human participants (N=28) can recognize the same set of actions accurately with all three versions of the stimuli, and perform significantly better on stimuli that show only the body than on stimuli that show only the background. Finally, we implement and test a novel architecture patterned after domain specificity in the brain with separate streams to process body and background information. We show that 1) this architecture improves action recognition performance, and 2) its accuracy across different versions of the stimuli follows a pattern that matches more closely the pattern of accuracy observed in human participants.

