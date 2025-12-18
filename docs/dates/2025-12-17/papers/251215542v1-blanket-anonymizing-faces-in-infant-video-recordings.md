---
layout: default
title: BLANKET: Anonymizing Faces in Infant Video Recordings
---

# BLANKET: Anonymizing Faces in Infant Video Recordings
**arXiv**：[2512.15542v1](https://arxiv.org/abs/2512.15542) · [PDF](https://arxiv.org/pdf/2512.15542.pdf)  
**作者**：Ditmar Hadera, Jan Cech, Miroslav Purkrabek, Matej Hoffmann  

**一句话要点**：提出BLANKET方法以匿名化婴儿视频中的面部，同时保留关键面部属性。

**关键词**：婴儿面部匿名化, 扩散模型, 时间一致性, 面部属性保留, 视频处理

## 3 点简述
- 核心问题：婴儿视频数据伦理使用需匿名化，但现有方法可能破坏面部属性。
- 方法要点：采用两阶段流程，先通过扩散模型生成兼容新身份，再通过时间一致的面部交换实现无缝替换。
- 实验或效果：在婴儿视频数据集上评估，优于DeepPrivacy2，在去识别、属性保留、下游任务影响和伪影方面表现更佳。

## 摘要（原文）

> Ensuring the ethical use of video data involving human subjects, particularly infants, requires robust anonymization methods. We propose BLANKET (Baby-face Landmark-preserving ANonymization with Keypoint dEtection consisTency), a novel approach designed to anonymize infant faces in video recordings while preserving essential facial attributes. Our method comprises two stages. First, a new random face, compatible with the original identity, is generated via inpainting using a diffusion model. Second, the new identity is seamlessly incorporated into each video frame through temporally consistent face swapping with authentic expression transfer. The method is evaluated on a dataset of short video recordings of babies and is compared to the popular anonymization method, DeepPrivacy2. Key metrics assessed include the level of de-identification, preservation of facial attributes, impact on human pose estimation (as an example of a downstream task), and presence of artifacts. Both methods alter the identity, and our method outperforms DeepPrivacy2 in all other respects. The code is available as an easy-to-use anonymization demo at https://github.com/ctu-vras/blanket-infant-face-anonym.

