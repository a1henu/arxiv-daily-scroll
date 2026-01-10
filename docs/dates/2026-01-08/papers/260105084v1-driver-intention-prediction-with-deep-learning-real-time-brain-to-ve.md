---
layout: default
title: Driver-Intention Prediction with Deep Learning: Real-Time Brain-to-Vehicle Communication
---

# Driver-Intention Prediction with Deep Learning: Real-Time Brain-to-Vehicle Communication
**arXiv**：[2601.05084v1](https://arxiv.org/abs/2601.05084) · [PDF](https://arxiv.org/pdf/2601.05084.pdf)  
**作者**：Niloufar Alavi, Swati Shah, Rezvan Alamian, Stefan Goetz  

**一句话要点**：提出基于深度学习的脑电信号方法，实时预测驾驶员转向意图以增强车辆辅助系统。

**关键词**：脑机接口, 驾驶员意图预测, 脑电信号分类, 卷积神经网络, 驾驶辅助系统, 实时通信

## 3 点简述
- 核心问题：如何利用脑机接口快速预测驾驶员转向意图，提升驾驶辅助系统的响应速度。
- 方法要点：使用卷积神经网络对原始脑电信号进行最小预处理，分类左转、右转和直行三种意图。
- 实验或效果：在驾驶模拟器中实现83.7%的分类准确率，右转识别率最高，表明脑活动可能存在空间偏差。

## 摘要（原文）

> Brain-computer interfaces (BCIs) allow direct communication between the brain and electronics without the need for speech or physical movement. Such interfaces can be particularly beneficial in applications requiring rapid response times, such as driving, where a vehicle's advanced driving assistance systems could benefit from immediate understanding of a driver's intentions. This study presents a novel method for predicting a driver's intention to steer using electroencephalography (EEG) signals through deep learning. A driving simulator created a controlled environment in which participants imagined controlling a vehicle during various driving scenarios, including left and right turns, as well as straight driving. A convolutional neural network (CNN) classified the detected EEG data with minimal pre-processing. Our model achieved an accuracy of 83.7% in distinguishing between the three steering intentions and demonstrated the ability of CNNs to process raw EEG data effectively. The classification accuracy was highest for right-turn segments, which suggests a potential spatial bias in brain activity. This study lays the foundation for more intuitive brain-to-vehicle communication systems.

