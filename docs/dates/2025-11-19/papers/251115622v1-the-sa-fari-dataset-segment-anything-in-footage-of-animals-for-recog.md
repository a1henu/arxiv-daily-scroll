---
layout: default
title: The SA-FARI Dataset: Segment Anything in Footage of Animals for Recognition and Identification
---

# The SA-FARI Dataset: Segment Anything in Footage of Animals for Recognition and Identification
**arXiv**：[2511.15622v1](https://arxiv.org/abs/2511.15622) · [PDF](https://arxiv.org/pdf/2511.15622.pdf)  
**作者**：Dante Francisco Wasmuht, Otto Brookes, Maximillian Schall, Pablo Palencia, Chris Beirne, Tilo Burghardt, Majid Mirmehdi, Hjalmar Kühl, Mimi Arandjelovic, Sam Pottie, Peter Bermant, Brandon Asheim, Yi Jin Toh, Adam Elzinga, Jason Holmberg, Andrew Whitworth, Eleanor Flatt, Laura Gustafson, Chaitanya Ryali, Yuan-Ting Hu, Baishan Guo, Andrew Westbury, Kate Saenko, Didac Suris  

**一句话要点**：提出SA-FARI数据集以解决野生动物多动物追踪基准缺失问题

**关键词**：多动物追踪, 野生动物数据集, 分割掩码, 物种识别, 基准测试, 计算机视觉

## 3 点简述
- 现有数据集规模小、物种少，缺乏时空多样性，无法训练通用多动物追踪模型
- SA-FARI包含11,609个视频，覆盖99个物种，提供密集边界框、分割掩码和物种标注
- 使用SAM 3等模型进行基准测试，评估物种特定和通用动物提示下的检测与追踪性能

## 摘要（原文）

> Automated video analysis is critical for wildlife conservation. A foundational task in this domain is multi-animal tracking (MAT), which underpins applications such as individual re-identification and behavior recognition. However, existing datasets are limited in scale, constrained to a few species, or lack sufficient temporal and geographical diversity - leaving no suitable benchmark for training general-purpose MAT models applicable across wild animal populations. To address this, we introduce SA-FARI, the largest open-source MAT dataset for wild animals. It comprises 11,609 camera trap videos collected over approximately 10 years (2014-2024) from 741 locations across 4 continents, spanning 99 species categories. Each video is exhaustively annotated culminating in ~46 hours of densely annotated footage containing 16,224 masklet identities and 942,702 individual bounding boxes, segmentation masks, and species labels. Alongside the task-specific annotations, we publish anonymized camera trap locations for each video. Finally, we present comprehensive benchmarks on SA-FARI using state-of-the-art vision-language models for detection and tracking, including SAM 3, evaluated with both species-specific and generic animal prompts. We also compare against vision-only methods developed specifically for wildlife analysis. SA-FARI is the first large-scale dataset to combine high species diversity, multi-region coverage, and high-quality spatio-temporal annotations, offering a new foundation for advancing generalizable multianimal tracking in the wild. The dataset is available at $\href{https://www.conservationxlabs.com/sa-fari}{\text{conservationxlabs.com/SA-FARI}}$.

