NAME="DjangoBlog"
DJANGODIR=/home/pi/DjangoBlog # Django项目文件夹
USER=pi # 用户
GROUP=pi # 用户组
NUM_WORKERS=1 # Gunicorn应该生成多少个工作进程
DJANGO_SETTINGS_MODULE=DjangoBlog.settings # Django使用的配置文件
DJANGO_WSGI_MODULE=DjangoBlog.wsgi # WSGI 模块名称

echo "Starting $NAME as `whoami`"

# 激活虚拟环境步骤
cd $DJANGODIR
source /home/pi/PythonVenv/djangoblog/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# 如果运行目录不存在，则创建
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# 启动 Django Unicorn
# 要在管理器下运行的程序不应对自身进行后台监控（不要使用--daemon）
exec /home/pi/PythonVenv/djangoblog/bin/gunicorn  ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=debug \
--log-file=-