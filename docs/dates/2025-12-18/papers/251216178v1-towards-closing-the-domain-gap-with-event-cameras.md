---
layout: default
title: Towards Closing the Domain Gap with Event Cameras
---

# Towards Closing the Domain Gap with Event Cameras
**arXiv**：[2512.16178v1](https://arxiv.org/abs/2512.16178) · [PDF](https://arxiv.org/pdf/2512.16178.pdf)  
**作者**：M. Oltan Sevinc, Liao Wu, Francisco Cruz  

**一句话要点**：提出事件相机以解决自动驾驶中昼夜光照差异的域差距问题

**关键词**：事件相机, 域差距, 自动驾驶, 光照差异, 跨域性能

## 3 点简述
- 核心问题：传统相机在训练与部署环境不匹配时性能下降，即域差距，特别是昼夜光照差异。
- 方法要点：使用事件相机替代传统相机，无需额外调整即可跨光照条件保持性能。
- 实验或效果：事件相机在跨域场景中性能更一致，域偏移惩罚通常与灰度帧相当或更小，并提供更优基线性能。

## 摘要（原文）

> Although traditional cameras are the primary sensor for end-to-end driving, their performance suffers greatly when the conditions of the data they were trained on does not match the deployment environment, a problem known as the domain gap. In this work, we consider the day-night lighting difference domain gap. Instead of traditional cameras we propose event cameras as a potential alternative which can maintain performance across lighting condition domain gaps without requiring additional adjustments. Our results show that event cameras maintain more consistent performance across lighting conditions, exhibiting domain-shift penalties that are generally comparable to or smaller than grayscale frames and provide superior baseline performance in cross-domain scenarios.

