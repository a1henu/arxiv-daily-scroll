---
layout: default
title: Towards Generative Location Awareness for Disaster Response: A Probabilistic Cross-view Geolocalization Approach
---

# Towards Generative Location Awareness for Disaster Response: A Probabilistic Cross-view Geolocalization Approach
**arXiv**：[2512.20056v1](https://arxiv.org/abs/2512.20056) · [PDF](https://arxiv.org/pdf/2512.20056.pdf)  
**作者**：Hao Li, Fabian Deuser, Wenping Yin, Steffen Knoblauch, Wufan Zhao, Filip Biljecki, Yong Xue, Wei Huang  

**一句话要点**：提出ProbGLC概率跨视图地理定位方法，以增强灾害响应中的位置感知能力。

**关键词**：跨视图地理定位, 灾害响应, 概率模型, 不确定性量化, 生成式位置感知

## 3 点简述
- 核心问题：灾害响应中需快速准确识别灾害位置，支持决策与资源分配。
- 方法要点：结合概率与确定性模型，提升模型可解释性并实现先进地理定位性能。
- 实验或效果：在MultiIAN和SAGAINDisaster数据集上验证，准确率高且提供概率分布和可定位性评分。

## 摘要（原文）

> As Earth's climate changes, it is impacting disasters and extreme weather events across the planet. Record-breaking heat waves, drenching rainfalls, extreme wildfires, and widespread flooding during hurricanes are all becoming more frequent and more intense. Rapid and efficient response to disaster events is essential for climate resilience and sustainability. A key challenge in disaster response is to accurately and quickly identify disaster locations to support decision-making and resources allocation. In this paper, we propose a Probabilistic Cross-view Geolocalization approach, called ProbGLC, exploring new pathways towards generative location awareness for rapid disaster response. Herein, we combine probabilistic and deterministic geolocalization models into a unified framework to simultaneously enhance model explainability (via uncertainty quantification) and achieve state-of-the-art geolocalization performance. Designed for rapid diaster response, the ProbGLC is able to address cross-view geolocalization across multiple disaster events as well as to offer unique features of probabilistic distribution and localizability score. To evaluate the ProbGLC, we conduct extensive experiments on two cross-view disaster datasets (i.e., MultiIAN and SAGAINDisaster), consisting diverse cross-view imagery pairs of multiple disaster types (e.g., hurricanes, wildfires, floods, to tornadoes). Preliminary results confirms the superior geolocalization accuracy (i.e., 0.86 in Acc@1km and 0.97 in Acc@25km) and model explainability (i.e., via probabilistic distributions and localizability scores) of the proposed ProbGLC approach, highlighting the great potential of leveraging generative cross-view approach to facilitate location awareness for better and faster disaster response. The data and code is publicly available at https://github.com/bobleegogogo/ProbGLC

