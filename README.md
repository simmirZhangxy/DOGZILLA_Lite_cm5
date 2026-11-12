# DOGZILLA Lite CM5

亚博 DOGZILLA-Lite（树莓派 CM5）课程与示例代码备份。

- 课程：[DOGZILLA-Lite 学习页](https://www.yahboom.com/study/DOGZILLA-Lite)
- 上游参考：`RaspberryPi-CM4-main` 来自 [Xgorobot/RaspberryPi-CM4](https://github.com/Xgorobot/RaspberryPi-CM4)

## 仓库内容

| 目录 | 说明 |
|------|------|
| `DOGZILLA_Lite_class/` | 官方课程 Jupyter / Python（基础控制、OpenCV、视觉识别与交互等） |
| `RaspberryPi-CM4-main/` | 机身菜单 Demo、语音、智能体等（CM5 出厂镜像中目录名常为 `RaspberryPi-CM5`） |
| `XGO-lite3_URDF_v2026.09.17/` | XGO-lite3 仿真 URDF |
| `XGO通讯接口表.xlsx` | 通讯接口说明 |

## 未纳入 Git 的内容

见根目录 `.gitignore`。克隆后需自行准备的内容主要是 **`model/`**（约 1.5GB），以避免超出 GitHub 体积与单文件限制。

板上运行时，许多脚本硬编码路径 **`/home/pi/model/...`**，请保持目录结构与下表一致。

### `model/` 文件清单

| 文件 / 目录 | 典型用途 |
|-------------|----------|
| `Model.onnx` | YOLO 检测、人体跟随等 |
| `msyh.ttc`、`platech.ttf` | 中文显示、车牌识别相关 |
| `age_deploy.prototxt`、`age_net.caffemodel` | 年龄估计 |
| `gender_deploy.prototxt`、`gender_net.caffemodel` | 性别估计 |
| `opencv_face_detector.pbtxt`、`opencv_face_detector_uint8.pb` | OpenCV DNN 人脸 |
| `EmotionDetectionModel.h5` | 情绪识别 |
| `frozen_inference_graph.pb` | TensorFlow 目标检测 |
| `ssdlite_mobilenet_v2_coco_2018_05_09/` | SSD Lite MobileNet V2（COCO） |
| `object_detection_ssd_mobilenetv2_oidv4_fp16.tflite` | TFLite 检测 |
| `pose_landmark_heavy.tflite` | 人体姿态 |
| `haarcascade_frontalface_default.xml`、`Facefile/` | Haar 人脸级联 |
| `data/`、`object_detection_coco.txt`、`ssd_mobilenet_v2_coco.txt` | 标签与配置 |
| `model.zip` | 官方打包（若提供，解压后与上述结构对齐即可） |

请勿使用重复的 `model copy/` 目录，与 `model/` 内容重复。

### 如何获取 `model/`

1. **推荐**：亚博 DOGZILLA-Lite **产品资料** 或 **出厂 CM5 镜像** 中的 `/home/pi/model`，复制到本仓库根目录：`./model/`。
2. **从机子拷贝**（将 `<IP>` 换成狗在局域网内的地址）：

   ```bash
   scp -r pi@<IP>:/home/pi/model ./model
   ```

3. **部分 SSD 模型**：课程 `DOGZILLA_Lite_class/5.AI Visual Recognition Course/04. Object recognition/README.md` 中有 TensorFlow Model Zoo 下载说明；字体与 ONNX 等定制资源仍以亚博资料包为准。

## 运行环境（简要）

- 硬件：DOGZILLA-Lite + CM5 等亚博配套环境
- Python：`xgolib` / `xgo-pythonlib`、`picamera2`、OpenCV 等（以官方镜像或课程文档为准）
- 升级控制库：

  ```bash
  pip install --upgrade xgo-pythonlib
  sudo pip install --upgrade xgo-pythonlib
  ```

菜单「你放我捡」对应 `RaspberryPi-CM4-main/demos/mypick_it_up.py`；课程第 11 课抓取示例见 `DOGZILLA_Lite_class/6.AI Visual Interaction Course/11.pick it up/`。

## API 密钥（Demo 用）

部分语音/大模型 Demo 读取 `RaspberryPi-CM4-main/demos/API_KEY.py`。**该文件不入库**。

```bash
cp RaspberryPi-CM4-main/demos/API_KEY.example.py RaspberryPi-CM4-main/demos/API_KEY.py
# 编辑 API_KEY.py，填入自己的 key，勿提交到 Git
```

## 克隆与本仓库协作

```bash
git clone https://github.com/simmirZhangxy/DOGZILLA_Lite_cm5.git
cd DOGZILLA_Lite_cm5
cp RaspberryPi-CM4-main/demos/API_KEY.example.py RaspberryPi-CM4-main/demos/API_KEY.py
# 按上文准备 model/ 后再运行课程或 demos
```

## 版权说明

课程代码、模型及商标版权归亚博智能及相应原作者。本仓库仅供个人学习备份；再分发或商用请遵循官方许可与协议。
