---
layout: default
title: RGBT-Ground Benchmark: Visual Grounding Beyond RGB in Complex Real-World Scenarios
---

# RGBT-Ground Benchmark: Visual Grounding Beyond RGB in Complex Real-World Scenarios
**arXiv**：[2512.24561v1](https://arxiv.org/abs/2512.24561) · [PDF](https://arxiv.org/pdf/2512.24561.pdf)  
**作者**：Tianyi Zhao, Jiawen Xi, Linhui Xiao, Junnan Li, Xue Yang, Maoxun Yuan, Xingxing Wei  

**一句话要点**：提出RGBT-Ground基准与RGBT-VGNet框架，以解决复杂现实场景下的视觉定位问题。

**关键词**：视觉定位, 多模态融合, 热红外图像, 复杂场景基准, 鲁棒性评估

## 3 点简述
- 现有视觉定位基准局限于清洁环境，无法评估模型在光照变化等复杂条件下的鲁棒性。
- 构建首个大规模RGB-热红外对齐基准，支持单模态与多模态输入，并设计RGBT-VGNet融合互补视觉信息。
- 实验表明RGBT-VGNet在夜间和远距离场景中显著优于现有方法，基准将公开以促进研究。

## 摘要（原文）

> Visual Grounding (VG) aims to localize specific objects in an image according to natural language expressions, serving as a fundamental task in vision-language understanding. However, existing VG benchmarks are mostly derived from datasets collected under clean environments, such as COCO, where scene diversity is limited. Consequently, they fail to reflect the complexity of real-world conditions, such as changes in illumination, weather, etc., that are critical to evaluating model robustness and generalization in safety-critical applications. To address these limitations, we present RGBT-Ground, the first large-scale visual grounding benchmark built for complex real-world scenarios. It consists of spatially aligned RGB and Thermal infrared (TIR) image pairs with high-quality referring expressions, corresponding object bounding boxes, and fine-grained annotations at the scene, environment, and object levels. This benchmark enables comprehensive evaluation and facilitates the study of robust grounding under diverse and challenging conditions. Furthermore, we establish a unified visual grounding framework that supports both uni-modal (RGB or TIR) and multi-modal (RGB-TIR) visual inputs. Based on it, we propose RGBT-VGNet, a simple yet effective baseline for fusing complementary visual modalities to achieve robust grounding. We conduct extensive adaptations to the existing methods on RGBT-Ground. Experimental results show that our proposed RGBT-VGNet significantly outperforms these adapted methods, particularly in nighttime and long-distance scenarios. All resources will be publicly released to promote future research on robust visual grounding in complex real-world environments.

